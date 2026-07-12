from ..ai.models import AIRequest, AIResponse
from ..ai.providers import get_provider_registry
from ..ai.exceptions import ProviderNotSupportedError

class AIService:
    """Service layer untuk generasi AI. Menggunakan provider registry."""

    def __init__(self, provider_name: str = "gemini"):
        self.provider_name = provider_name
        self.client = get_provider_registry().get_client(provider_name)

    async def initialize(self) -> None:
        """Inisialisasi provider AI (misal, menyiapkan koneksi)."""
        await self.client.initialize()

    async def generate(self, request: AIRequest) -> AIResponse:
        """Generate konten menggunakan provider yang dipilih."""
        # Pastikan client sudah diinisialisasi (dapat dipanggil di startup)
        if not self.client._initialized:
            await self.initialize()
        try:
            return await self.client.generate(request)
        except NotImplementedError:
            return AIResponse(
                response_text="",
                provider=self.provider_name,
                error="AI generation is not yet implemented."
            )