import os
from pathlib import Path
from src.core.pdf_to_docx import PDFToDOCX
from src.core.pdf_to_csv import PDFToCSV

def test_pdf_to_docx(sample_pdfs, tmp_path):
    conv=PDFToDOCX()
    out=tmp_path / "out.docx"
    summary=conv.convert(str(sample_pdfs["text"]),str(out))
    assert out.exists()
    assert summary["total"]>0
    # scanned page may fail OCR, check summary includes 1 if fallback needed

def test_pdf_to_csv(sample_pdfs, tmp_path):
    conv=PDFToCSV()
    out=tmp_path / "out.csv"
    summary=conv.convert(str(sample_pdfs["text"]),str(out))
    assert out.exists()
