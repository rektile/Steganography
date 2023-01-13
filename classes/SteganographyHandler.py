import numpy as np
from PIL import Image

class SteganographyHandler:

    def __init__(self):

        self.endingMarker = "$;87"
        self.inputPath = None
        self.outputPath = None
        self.secretMessage = None
        self.encodeMode = None

    def argumentParser(self, args):

        if not args.encode and not args.decode:
            print("[!] You need to select encode or decode mode.")
            exit()

        if not args.input:
            print("[!] You need to specify an image you want to use.")
            exit()

        if args.encode and not args.output:
            print("[!] You need to specify the output path.")
            exit()

        if args.encode and not args.secret:
            print("[!] You need to specify your secret message.")
            exit()

        self.inputPath = args.input
        self.outputPath = args.output
        self.secretMessage = args.secret
        self.encodeMode = args.encode


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

        return totalSpace >= len(messageBits)

    def decode(self, imageArray):

        messageBits = ""

        for row in imageArray:

            for pixel in row:

                for channel in pixel:

                    lastBit = self.getBitFromChannel(channel)
                    messageBits += str(lastBit)
                    decodedMessage = self.binaryToString(messageBits)
                    if decodedMessage.endswith(self.endingMarker):
                        return decodedMessage.replace(self.endingMarker, "")

        return None

    def encode(self, imageArray, messageBits):

        messageIndex = 0

        for rowIndex, row in enumerate(imageArray):

            for pixelIndex, pixel in enumerate(row):

                for channelIndex, channel in enumerate(pixel):

                    if messageIndex < len(messageBits):
                        currentMessageBit = messageBits[messageIndex]
                        modifiedChannel = self.setBitInChannel(channel, currentMessageBit)
                        messageIndex += 1
                        imageArray[rowIndex][pixelIndex][channelIndex] = modifiedChannel
                    else:
                        return imageArray

        return imageArray

    def getBitFromChannel(self, channel):
        lastBit = channel & 1
        return lastBit

    def setBitInChannel(self, channel, bit):
        if bit == "1":
            channel |= 1
        elif bit == "0":
            channel &= ~1
        return channel

    def saveImageFromArray(self, imageArray, imageName):
        img = Image.fromarray(imageArray)
        img.save(imageName)

    def run(self):

        imageArray = self.getPixelsFromImage(self.inputPath)

        if self.encodeMode:
            print(f"[*] Encoding message \"{self.secretMessage}\" into image {self.inputPath}")


            secretWithMarker = self.secretMessage + self.endingMarker

            secretBits = self.stringToBinary(secretWithMarker)

            if not self.checkIfFits(imageArray, secretBits):
                print(f"[!] Not enough space inside the image.")
                exit()

            modifiedImageArray = self.encode(imageArray, secretBits)
            print(f"[*] Saving new image to {self.outputPath}")
            self.saveImageFromArray(modifiedImageArray, self.outputPath)
        else:
            foundSecretMessage = self.decode(imageArray)
            if foundSecretMessage:
                print(f"[*] Secret message is: {foundSecretMessage}")
            else:
                print(f"[!] Couldn't find secret message.")