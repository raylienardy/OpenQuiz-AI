from typing import Dict, Type, Optional
from .base_client import BaseAIClient
from .gemini_client import GeminiClient

class AIProviderRegistry:
    """Registry for AI provider clients. New providers can be registered here."""

    def __init__(self):
        self._providers: Dict[str, Type[BaseAIClient]] = {
            "gemini": GeminiClient,
        }

    def get_client(self, provider_name: str) -> BaseAIClient:
        provider_class = self._providers.get(provider_name.lower())
        if not provider_class:
            from .exceptions import ProviderNotSupportedError
            raise ProviderNotSupportedError(f"Provider '{provider_name}' is not supported.")
        return provider_class()

    def register(self, name: str, client_class: Type[BaseAIClient]) -> None:
        self._providers[name.lower()] = client_class

# Global instance (atau bisa dibuat via dependency injection)
_provider_registry = None

def get_provider_registry() -> AIProviderRegistry:
    global _provider_registry
    if _provider_registry is None:
        _provider_registry = AIProviderRegistry()
    return _provider_registry