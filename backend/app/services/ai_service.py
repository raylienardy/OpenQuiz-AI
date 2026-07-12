from ..ai.models import AIRequest, AIResponse
from ..ai.providers import get_provider_registry
from ..config import get_settings

class AIService:
    def __init__(self):
        settings = get_settings()
        self.provider_name = settings.ai_provider
        self.client = get_provider_registry().get_client(self.provider_name)

    async def initialize(self) -> None:
        await self.client.initialize()

    async def generate(self, request: AIRequest) -> AIResponse:
        # Pastikan inisialisasi sudah dipanggil (bisa juga dipanggil di startup)
        if not self.client._client:
            await self.initialize()
        return await self.client.generate(request)