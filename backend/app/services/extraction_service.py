from fastapi import UploadFile
from ..extractors.factory import ExtractorFactory
from ..extractors.models import ExtractionResult

class ExtractionService:
    """Orchestrates extraction: gets extractor, calls it, then populates statistics."""

    async def extract(self, file: UploadFile) -> ExtractionResult:
        if not file.filename:
            raise ValueError("File has no name, cannot determine type")

        # Dapatkan extractor dari factory
        extractor = ExtractorFactory.get_extractor(file.filename)

        # Jalankan ekstraksi (hasil mentah)
        result = await extractor.extract(file)

        # Perkaya hasil dengan statistik jika teks tidak kosong
        if result.text:
            result.character_count = len(result.text)
            result.word_count = len(result.text.split())
        # Metadata (page_count) sudah diisi oleh extractor jika tersedia

        return result