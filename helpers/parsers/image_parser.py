import pytesseract
from PIL import Image
from langchain.schema import Document

def parse_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return [Document(page_content=text)]
