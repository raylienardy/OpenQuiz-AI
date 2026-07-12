from fastapi import UploadFile
from ..extractors.factory import ExtractorFactory
from ..extractors.models import ExtractionResult
from ..text_processing.pipeline import clean_text

class ExtractionService:
    """Orchestrates extraction: gets extractor, calls it, then cleans and enriches."""

    async def extract(self, file: UploadFile) -> ExtractionResult:
        if not file.filename:
            raise ValueError("File has no name, cannot determine type")

        # Dapatkan extractor dari factory
        extractor = ExtractorFactory.get_extractor(file.filename)

        # Jalankan ekstraksi (hasil mentah)
        result = await extractor.extract(file)

        # Bersihkan teks mentah menggunakan pipeline
        if result.text:
            result.text = clean_text(result.text)

        # Perkaya hasil dengan statistik berdasarkan teks yang sudah bersih
        if result.text:
            result.character_count = len(result.text)
            result.word_count = len(result.text.split())

        return result