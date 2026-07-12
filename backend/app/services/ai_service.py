from ..ai.models import AIRequest, AIResponse
from ..ai.providers import get_provider_registry
from ..ai.exceptions import ProviderNotSupportedError

class AIService:
    """Service layer for AI generation. Uses the provider registry."""

    def __init__(self, provider_name: str = "gemini"):
        self.provider_name = provider_name
        self.client = get_provider_registry().get_client(provider_name)

    async def generate(self, request: AIRequest) -> AIResponse:
        try:
            return await self.client.generate(request)
        except NotImplementedError:
            # Placeholder hingga provider benar-benar terimplementasi
            return AIResponse(
                response_text="",
                provider=self.provider_name,
                error="AI generation is not yet implemented."
            )