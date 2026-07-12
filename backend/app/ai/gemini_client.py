from .base_client import BaseAIClient
from .models import AIRequest, AIResponse

class GeminiClient(BaseAIClient):
    """Placeholder for Google Gemini integration."""

    async def initialize(self) -> None:
        # TODO: Inisialisasi SDK Gemini
        pass

    async def generate(self, request: AIRequest) -> AIResponse:
        # TODO: Kirim prompt ke Gemini, dapatkan respons
        raise NotImplementedError("GeminiClient.generate() not yet implemented")

    async def health_check(self) -> bool:
        # TODO: Panggil endpoint health Gemini jika tersedia
        return False

    async def close(self) -> None:
        # TODO: Tutup koneksi jika perlu
        pass