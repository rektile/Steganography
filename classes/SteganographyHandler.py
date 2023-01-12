import numpy as np
from PIL import Image

class SteganographyHandler:

    def __init__(self):

        self.endingMarker = "$;87"

    def stringToBinary(self, text):
        return "".join(format(ord(char), "08b") for char in str(text))

    def binaryToString(self, binary):
        return "".join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    def getPixelsFromImage(self, imagePath):
        with Image.open(imagePath) as img:
            data = np.array(img)

        return data


    def run(self):



        binary = self.stringToBinary("text")
        print(binary)

        text = self.binaryToString(binary)
        print(text)

