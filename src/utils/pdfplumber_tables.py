import pdfplumber

def detect_tables(pdf_path):
    """Return a dict mapping page number to list of table data lists."""
    tables = {}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_tables = page.find_tables(
                table_settings={
                    'vertical_strategy': 'text',
                    'horizontal_strategy': 'text',
                    'min_words_vertical': 4,
                    'min_words_horizontal': 2
                }
            )
            tbls = []
            for tbl in page_tables:
                data = tbl.extract()
                tbls.append(data)
            if tbls:
                tables[i] = tbls
    return tables