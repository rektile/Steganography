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


    def run(self):

        imageArray = self.getPixelsFromImage(self.imageName)

        secretWithMarker = self.secretMessage + self.endingMarker

        secretBits = self.stringToBinary(secretWithMarker)


