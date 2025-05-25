import os
from helpers.parsers.pdf_parser import parse_pdf
from helpers.parsers.txt_parser import parse_txt
from helpers.parsers.image_parser import parse_image
from helpers.parsers.url_parser import parse_url

def parse_input(file=None, url=None):
    if url:
        return parse_url(url)
    
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.pdf':
        return parse_pdf(file)
    elif ext == '.txt':
        return parse_txt(file)
    elif ext in ['.png', '.jpg', '.jpeg']:
        return parse_image(file)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
