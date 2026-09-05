# PDF Toolkit

**Version 0.1 – Fri Sep 04 2026**

The PDF Toolkit is a small Windows‑only application that converts PDF documents into either DOCX or CSV files.

## How it works
* **PDF → DOCX** – Uses `pdf2docx` for text extraction. If a page has no text layer, the tool falls back to OCR via Tesseract and appends the recognized text to the resulting Word document.
* **PDF → CSV** – Tries to extract tables with `camelot‑py`. When no table is found, it runs OCR on the page and writes each line of recognised text as a single‑column row in the CSV file.

The GUI is built with Tkinter; simply double‑click the generated `.exe` (or run `python src/gui/main_window.py`) to launch. Choose a PDF, pick an output format, and watch the progress bar.

## Requirements
* **Python 3.11**
* Python packages listed in `requirements.txt`. Install with:
  ```bash
  pip install -r requirements.txt
  ```
* **Ghostscript** – required by camelot‑py. Download from https://www.ghostscript.com/download/gsdnld.html and add the bin folder to your PATH.
* **Tesseract OCR** – installed at `C:\Program Files\Tesseract-OCR`. The tool automatically uses this location.

## Known issues
* The application is Windows‑only; it relies on PowerShell for packaging and cannot be run natively on Linux/macOS without modifications.
* OCR quality depends heavily on the source PDF. Scanned documents with low resolution may produce incomplete text or tables.

Happy converting!