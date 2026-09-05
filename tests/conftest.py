import os
from pathlib import Path
import pytest

def generate_text_pdf(path:Path):
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(str(path))
    c.drawString(100, 750, "Sample Text Page")
    c.showPage()
    c.save()

def generate_scanned_pdf(path:Path):
    from PIL import Image
    img = Image.new('RGB', (600, 800), color='white')
    img_path=path.with_suffix('.png')
    img.save(img_path)
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(str(path))
    c.drawImage(str(img_path),0,0,600,800)
    c.showPage()
    c.save()
    img_path.unlink()  # remove temp image

@pytest.fixture(scope="session")
def sample_pdfs(tmp_path_factory):
    base=tmp_path_factory.mktemp("data")
    text_pdf=base / "text_page.pdf"
    scanned_pdf=base / "scanned_page.pdf"
    generate_text_pdf(text_pdf)
    generate_scanned_pdf(scanned_pdf)
    return {"text": text_pdf, "scanned": scanned_pdf}
