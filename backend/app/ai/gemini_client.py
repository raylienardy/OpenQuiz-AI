"""
Gemini AI Client – inisialisasi dan komunikasi dengan Google Gemini.
"""

import logging
from typing import Optional

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from .base_client import BaseAIClient
from .models import AIRequest, AIResponse
from .exceptions import (
    AIAuthenticationError,
    AIConnectionError,
    ProviderNotSupportedError,
)
from ..config import get_settings

logger = logging.getLogger(__name__)


class GeminiClient(BaseAIClient):
    """Implementasi Gemini menggunakan Google Generative AI SDK."""

    def __init__(self):
        self._model: Optional[genai.GenerativeModel] = None
        self._initialized = False
        self._model_name = "gemini-1.5-flash"  # model default yang cepat dan efisien

    async def initialize(self) -> None:
        """
        Baca API key dari konfigurasi, konfigurasikan SDK Gemini, dan siapkan model.
        Tidak melakukan panggilan jaringan.
        """
        if self._initialized:
            return

        settings = get_settings()
        api_key = settings.gemini_api_key

        # Validasi API key
        if not api_key or not api_key.strip():
            raise AIAuthenticationError(
                "Gemini API key is missing or empty. "
                "Set GEMINI_API_KEY in your .env file."
            )

        try:
            # Konfigurasi SDK secara global (aman untuk pemanggilan berulang)
            genai.configure(api_key=api_key.strip())
            # Instansiasi model
            self._model = genai.GenerativeModel(self._model_name)
            self._initialized = True
            logger.info("Gemini provider initialized successfully.")
        except Exception as e:
            # Tangkap semua error inisialisasi dan bungkus dengan exception kita
            raise AIConnectionError(
                f"Failed to initialize Gemini client: {str(e)}"
            ) from e

    async def generate(self, request: AIRequest) -> AIResponse:
        """Placeholder – akan diimplementasikan di task berikutnya."""
        if not self._initialized:
            raise AIConnectionError("Gemini client is not initialized.")
        # TODO: kirim prompt ke Gemini
        raise NotImplementedError("GeminiClient.generate() not yet implemented")

    async def health_check(self) -> bool:
        """Placeholder – akan memeriksa konektivitas nanti."""
        return self._initialized

    async def close(self) -> None:
        """Tidak ada resource yang perlu ditutup untuk Gemini."""
        pass