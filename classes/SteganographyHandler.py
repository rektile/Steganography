import numpy as np
from PIL import Image

class SteganographyHandler:

    def __init__(self, _imageName, _secretMessage):

        self.endingMarker = "$;87"
        self.imageName = _imageName
        self.secretMessage = _secretMessage

    def stringToBinary(self, text):
        return "".join(format(ord(char), "08b") for char in str(text))

    def binaryToString(self, binary):
        return "".join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    def getPixelsFromImage(self, imagePath):
        with Image.open(imagePath) as img:
            data = np.array(img)

        return data

    def checkIfFits(self, imageArray, messageBits):
        rows = len(imageArray)
        columns = len(imageArray[0])
        totalPixels = rows * columns
        totalSpace = totalPixels * 3

        return totalSpace >= messageBits

    def encode(self, imageArray, messageBits):

        messageIndex = 0

        for rowIndex, row in enumerate(imageArray):

            for pixelIndex, pixel in enumerate(row):

                for channelIndex, channel in enumerate(pixel):

                    if messageIndex < len(messageBits):
                        currentMessageBit = messageBits[messageIndex]
                        modifiedChannel = self.encodeInChannel(channel, currentMessageBit)
                        messageIndex += 1
                        imageArray[rowIndex][pixelIndex][channelIndex] = modifiedChannel
                    else:
                        return imageArray

        return imageArray

    def encodeInChannel(self, channel, bit):
        if bit == "1":
            channel |= 1
        elif bit == "0":
            channel &= ~1
        return channel


    def run(self):

        imageArray = self.getPixelsFromImage(self.imageName)

        secretWithMarker = self.secretMessage + self.endingMarker

        secretBits = self.stringToBinary(secretWithMarker)

        modifiedImageArray = self.encode(imageArray, secretBits)



