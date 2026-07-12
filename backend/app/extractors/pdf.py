from fastapi import UploadFile
from .base import BaseExtractor
from .models import ExtractionResult

class PDFExtractor(BaseExtractor):
    async def extract(self, file: UploadFile) -> ExtractionResult:
        """Placeholder: akan diimplementasikan dengan PyMuPDF nanti."""
        return ExtractionResult(
            file_type="pdf",
            warnings=["PDF extraction not yet implemented."]
        )