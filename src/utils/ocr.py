import pytesseract
from PIL import Image
# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(img: Image.Image) -> str:
    return pytesseract.image_to_string(img, lang='eng', config='--psm 6')
