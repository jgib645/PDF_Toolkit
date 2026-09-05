import pdfplumber
from pathlib import Path
class PDFPageLoader:
    def __init__(self, path: str):
        self.pdf = pdfplumber.open(path)
    def total_pages(self) -> int:
        return len(self.pdf.pages)
    def page_image(self, idx: int):
        return self.pdf.pages[idx].to_image().original
    def has_text_layer(self, idx: int) -> bool:
        return bool(self.pdf.pages[idx].extract_text())
