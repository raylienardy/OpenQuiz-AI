from fastapi import UploadFile
from ..extractors.factory import ExtractorFactory
from ..extractors.models import ExtractionResult

class ExtractionService:
    """Mengorkestrasi proses ekstraksi dari file yang diunggah."""
    
    async def extract(self, file: UploadFile) -> ExtractionResult:
        if not file.filename:
            raise ValueError("File has no name, cannot determine type")
        
        extractor = ExtractorFactory.get_extractor(file.filename)
        result = await extractor.extract(file)
        # Di masa depan bisa ditambahkan post-processing (pembersihan teks, dll.)
        return result