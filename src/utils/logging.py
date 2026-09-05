import logging
from pathlib import Path

def get_logger(name='pdf_toolkit', log_file_path=None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
        logger.addHandler(ch)
        if log_file_path:
            fh = logging.FileHandler(log_file_path, encoding='utf-8')
            fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            logger.addHandler(fh)
    return logger
