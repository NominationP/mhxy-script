import pytesseract
from PIL import Image
import os

def get_text(picture_path):
    # Set the TESSDATA_PREFIX environment variable
    os.environ['TESSDATA_PREFIX'] = '/usr/local/Cellar/tesseract/5.3.3/share/tessdata/'  # Replace with your tessdata directory

    # Path to your Tesseract-OCR executable (if installed via Homebrew)
    pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

    # Open an image file
    image = Image.open(picture_path)

    # Use Pytesseract to do OCR on the image with Chinese language
    text_tra = pytesseract.image_to_string(image, lang="chi_tra")
    text = pytesseract.image_to_string(image, lang="chi_sim")

    print("path: {}, image: {}, \ntra: {}, \nimage_to_string: {}".format(picture_path, image, text_tra, text))


if __name__ == '__main__':
    # Call the function with the path to your image
    # get_text('/Users/yibo/Documents/python/projects/pythonProject1/screenshot/网易mumu.png')
    get_text('/screenshot/checked_IMG_0222_PNG.rf.9a035c6481831619b56f8f8c9647640c.jpg')