from classes.SteganographyHandler import SteganographyHandler
import argparse

parser = argparse.ArgumentParser(prog="Steganography",
                                 description="Hide secret messages in a picture.")

parser.add_argument("-e",
                    "--encode",
                    help="Encoding mode.",
                    action='store_true')

parser.add_argument("-d",
                    "--decode",
                    help="Decoding mode.",
                    action='store_true')

parser.add_argument("-i",
                    "--input",
                    help="The image path you want to use to encode or decode.",
                    nargs="?")

parser.add_argument("-s",
                    "--secret",
                    help="The secret message you want to hide.",
                    nargs="?")

parser.add_argument("-o",
                    "--output",
                    help="The new image with the secret.",
                    nargs="?")

args = parser.parse_args()

stegHandler = SteganographyHandler()
stegHandler.argumentParser(args)
stegHandler.run()
