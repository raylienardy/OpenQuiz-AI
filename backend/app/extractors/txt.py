"""
TXT Extractor – reads plain text files with encoding fallback.
"""

from fastapi import UploadFile
from .base import BaseExtractor
from .models import ExtractionResult


class TXTExtractor(BaseExtractor):
    """Extract text from .txt files using multiple encoding attempts."""

    # Urutan encoding yang dicoba: UTF-8 (standar), UTF-8 dengan BOM, lalu Latin-1 (fallback universal)
    ENCODINGS = ["utf-8", "utf-8-sig", "latin-1"]

    async def extract(self, file: UploadFile) -> ExtractionResult:
        """
        Read the uploaded TXT file and return an ExtractionResult.
        Handles empty files, unknown encodings, and read errors.
        """
        warnings = []
        text = ""
        file_type = "txt"

        try:
            raw_bytes = await file.read()
        except Exception as e:
            # Jika pembacaan gagal (misal stream error)
            return ExtractionResult(
                text="",
                file_type=file_type,
                warnings=[f"Failed to read file: {str(e)}"],
            )

        # File kosong (0 byte)
        if not raw_bytes:
            return ExtractionResult(
                text="",
                file_type=file_type,
                warnings=["File is empty."],
            )

        # Coba decode dengan berbagai encoding
        decoded = None
        used_encoding = None
        for enc in self.ENCODINGS:
            try:
                decoded = raw_bytes.decode(enc)
                used_encoding = enc
                break
            except (UnicodeDecodeError, LookupError):
                continue

        if decoded is None:
            # Semua encoding gagal
            return ExtractionResult(
                text="",
                file_type=file_type,
                warnings=["Unable to decode file with supported encodings."],
            )

        # Sukses decode
        if used_encoding != "utf-8":
            warnings.append(
                f"File decoded using {used_encoding} instead of UTF-8."
            )

        # Hitung statistik dasar
        text = decoded
        character_count = len(text)
        word_count = len(text.split())

        return ExtractionResult(
            text=text,
            file_type=file_type,
            character_count=character_count,
            word_count=word_count,
            warnings=warnings,
        )