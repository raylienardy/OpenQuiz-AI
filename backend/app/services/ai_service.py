from ..ai.models import AIRequest, AIResponse
from ..ai.providers import get_provider_registry
from ..ai.exceptions import ProviderNotSupportedError, AIConnectionError
from ..config import get_settings

class AIService:
    """Service layer untuk generasi AI. Menggunakan provider dari konfigurasi."""

    def __init__(self):
        settings = get_settings()
        self.provider_name = settings.ai_provider
        self.client = get_provider_registry().get_client(self.provider_name)

    async def initialize(self) -> None:
        await self.client.initialize()

    async def generate(self, request: AIRequest) -> AIResponse:
        if not self.client._initialized:
            await self.initialize()
        return await self.client.generate(request)