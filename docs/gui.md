# PDF Toolkit GUI

## Prerequisites
1. **Python 3.11**
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ghostscript** – required by `camelot‑py`. Download from https://www.ghostscript.com/download/gsdnld.html and add the bin folder to your PATH.
4. **Tesseract OCR** – already installed at `C:\Program Files\Tesseract-OCR`.

## Running the Tool
```bash
python src/gui/main_window.py
```
A window will appear with two buttons:
- **PDF → DOCX**
- **PDF → CSV**
Select a PDF file; output will be saved next to the input with `_converted.docx` or `_converted.csv`. A log file (`*_converted.log`) is written alongside.

## Features
- Per‑page progress bar and status text.
- OCR fallback for pages without text layers (pdf2docx/camelot fail).
- Skipped pages are logged; a summary appears after conversion.
