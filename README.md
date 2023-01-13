# Steganography
 This is a simple tool that allows users to hide a text message within an image file.   
 The program uses the **least significant bit** technique to embed the message within the pixel data of the image.
## Installation
Clone the repository
```shell
git clone https://github.com/rektile/Simple-Image-Classifier.git
```

Go into the folder
```shell
cd ./Steganography
```

Install python requirements
```shell
pip install -r requirements.txt
```

## Usage
Encoding example
```shell
python Steganography.py -e -i image1.jpg -o image2.png -s "My secret message"
```
**Note:** Output needs to be PNG format

Decoding example
```shell
python Steganography.py -d -i image1.png
```
**Note:** Input needs to be PNG format