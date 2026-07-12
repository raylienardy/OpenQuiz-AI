from fastapi import UploadFile
from .base import BaseExtractor
from .models import ExtractionResult

class TXTExtractor(BaseExtractor):
    async def extract(self, file: UploadFile) -> ExtractionResult:
        """Placeholder: akan diimplementasikan dengan membaca konten langsung."""
        return ExtractionResult(
            file_type="txt",
            warnings=["TXT extraction not yet implemented."]
        )