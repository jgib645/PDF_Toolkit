from abc import ABC, abstractmethod
from typing import Callable, Optional

ProgressCallback = Callable[[int, int], None]

class Converter(ABC):
    @abstractmethod
    def convert(self,
                input_path: str,
                output_path: str,
                progress_cb: Optional[ProgressCallback] = None) -> dict:
        """
        Perform conversion.
        Returns a summary dict e.g. {'total': 12, 'failed_pages': [7]}
        """
        pass
