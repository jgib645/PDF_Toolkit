import camelot
import pandas as pd
from pdfplumber import PDF as PdfPlumberPDF
from ..utils.ocr import extract_text_from_image
from ..utils.logging import get_logger
from ..utils.pdf_reader import PDFPageLoader


class PDFToCSV:
    def convert(self, input_path: str, output_path: str, progress_cb=None) -> dict:
        logger = get_logger()
        loader = PDFPageLoader(input_path)
        total = loader.total_pages()
        all_tables = []
        failed = []

        for i in range(total):
            if progress_cb:
                progress_cb(i + 1, total)

            try:
                tables = camelot.read_pdf(input_path, pages=str(i + 1))

                if not tables:
                    # Fallback to OCR when camelot finds no tables on this page
                    logger.warning(f"No tables on page {i + 1}, OCR attempted")
                    img = loader.page_image(i)
                    text = extract_text_from_image(img)
                    lines = [l.strip() for l in text.splitlines() if l.strip()]
                    if lines:
                        df = pd.DataFrame(lines, columns=['text'])
                        all_tables.append(df)
                    else:
                        failed.append(i + 1)
                else:
                    for t in tables:
                        all_tables.append(t.df)

            except Exception as e:
                logger.error(f"Error processing page {i + 1}: {e}")
                failed.append(i + 1)

        if all_tables:
            df = pd.concat(all_tables, ignore_index=True)
            df.to_csv(output_path, index=False)

        return {'total': total, 'failed_pages': failed}
    