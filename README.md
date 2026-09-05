# PDF Toolkit

**Version 0.2 (in development) – Sep 2026**

The PDF Toolkit is a small Windows-only application that converts PDF documents into either DOCX or CSV files, with automatic fallback handling for scanned pages and borderless tables.

========================================================================
## How it works

* **PDF → DOCX** – Uses `pdf2docx` for text extraction. If a page has no text layer, the tool falls back to OCR via Tesseract and appends the recognized text to the resulting Word document. Tables detected via `pdfplumber` are appended as proper Word tables under a "Detected table (page X)" heading.
* **PDF → CSV** – Tries to extract bordered tables with `camelot-py` first. For pages without visible table borders, you can manually specify which page numbers contain tables; those pages are then processed with `pdfplumber`'s text-based table detection instead of relying on unreliable automatic guessing. Pages with no tables (bordered or manually flagged) fall back to OCR, with recognized text written as a single-column row.
* When conversion finishes, the tool opens File Explorer with the output file selected, and asks whether you'd like to open it immediately.

The GUI is built with Tkinter. Run it with `python -m src.gui.main_window` from the project root (packaging into a standalone `.exe` via PyInstaller is planned but not yet done). Choose a PDF, pick an output format, and watch the progress bar. For CSV conversion, you'll be asked to enter the page numbers (if any) that contain tables — this improves accuracy significantly over automatic detection.

========================================================================
## Requirements

* **Python 3.11**
* Python packages listed in `requirements.txt`. Install with:
```bash
  pip install -r requirements.txt
```
* **Ghostscript** – required by `camelot-py`. Download from https://www.ghostscript.com/download/gsdnld.html and add the `bin` folder to your PATH.
* **Tesseract OCR** – install from https://github.com/UB-Mannheim/tesseract/wiki. The tool expects it at `C:\Program Files\Tesseract-OCR\tesseract.exe` by default.

========================================================================
## Known issues

* The application is Windows-only and hasn't been tested on Linux/macOS.
* OCR quality depends heavily on the source PDF. Scanned documents with low resolution may produce incomplete text or tables.
* Automatic borderless-table detection proved unreliable (it either misses real tables or misidentifies plain paragraph text as a table). The current approach requires manually specifying which pages contain tables for the CSV converter — this is a deliberate design choice, not a bug, since accurate whitespace-based table detection without visible borders is a genuinely hard problem.
* Color icons/emoji (stored as color font glyphs) may convert to black-and-white outlines due to underlying PDF rendering library limitations. Standard colored text and images are unaffected.
* Standalone `.exe` packaging is not yet implemented — the tool currently runs from source only.

========================================================================
## Roadmap

* PyInstaller packaging for a standalone, double-clickable `.exe`
* Extend manual table-page selection to the DOCX converter's table detection
* CI pipeline for automated testing
  
========================================================================

Happy converting!
