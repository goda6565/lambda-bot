from dataclasses import dataclass
from typing import Optional


@dataclass
class PDFFile:
    url: str
    file_name: Optional[str] = None
    content: Optional[bytes] = None
    mime_type: str = "application/pdf"
    size: Optional[int] = None
