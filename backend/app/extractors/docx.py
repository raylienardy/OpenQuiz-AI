from fastapi import UploadFile
from .base import BaseExtractor
from .models import ExtractionResult

class DOCXExtractor(BaseExtractor):
    async def extract(self, file: UploadFile) -> ExtractionResult:
        """Placeholder: akan diimplementasikan dengan python-docx nanti."""
        return ExtractionResult(
            file_type="docx",
            warnings=["DOCX extraction not yet implemented."]
        )