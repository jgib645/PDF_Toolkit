import pandas as pd
import camelot
from ..utils.ocr import extract_text_from_image
from ..utils.logging import get_logger
from ..utils.pdf_reader import PDFPageLoader
from ..utils.pdfplumber_tables import detect_tables


class PDFToCSV:
    def convert(self, input_path: str, output_path: str, progress_cb=None, trusted_table_pages=None) -> dict:
        trusted_table_pages = trusted_table_pages or set()
        logger = get_logger()
        loader = PDFPageLoader(input_path)
        total = loader.total_pages()
        all_tables = []
        failed = []

        plumber_tables = {}
        if trusted_table_pages:
            try:
                plumber_tables = detect_tables(input_path)
            except Exception as e:
                logger.error(f"pdfplumber table detection failed: {e}")

        for i in range(total):
            page_num = i + 1
            if progress_cb:
                progress_cb(page_num, total)

            try:
                tables = camelot.read_pdf(input_path, pages=str(page_num))
                if tables:
                    for t in tables:
                        all_tables.append(t.df)
                elif page_num in trusted_table_pages and page_num in plumber_tables:
                    logger.warning(f"Using manually flagged table detection on page {page_num}")
                    for table_data in plumber_tables[page_num]:
                        df = pd.DataFrame(table_data)
                        all_tables.append(df)
                else:
                    img = loader.page_image(i)
                    text = extract_text_from_image(img)
                    lines = [l.strip() for l in text.splitlines() if l.strip()]
                    if lines:
                        df = pd.DataFrame(lines, columns=[0])
                        all_tables.append(df)
                    else:
                        failed.append(page_num)
            except Exception as e:
                logger.error(f"Error processing page {page_num}: {e}")
                failed.append(page_num)

        if all_tables:
            df = pd.concat(all_tables, ignore_index=True)
            df.to_csv(output_path, index=False)

        return {'total': total, 'failed_pages': failed}