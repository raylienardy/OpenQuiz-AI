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
    AIRateLimitError,
    AIResponseError,
    AITimeoutError,
)
from ..config import get_settings

logger = logging.getLogger(__name__)


class GeminiClient(BaseAIClient):
    """Implementasi Gemini menggunakan Google Generative AI SDK."""

    def __init__(self):
        self._model: Optional[genai.GenerativeModel] = None
        self._initialized = False
        # Baca model dari konfigurasi
        settings = get_settings()
        self._model_name = settings.gemini_model

    async def initialize(self) -> None:
        if self._initialized:
            return

        settings = get_settings()
        api_key = settings.gemini_api_key

        if not api_key or not api_key.strip():
            raise AIAuthenticationError(
                "Gemini API key is missing or empty. "
                "Set GEMINI_API_KEY in your .env file."
            )

        try:
            genai.configure(api_key=api_key.strip())
            self._model = genai.GenerativeModel(self._model_name)
            self._initialized = True
            logger.info("Gemini provider initialized successfully.")
        except Exception as e:
            raise AIConnectionError(
                f"Failed to initialize Gemini client: {str(e)}"
            ) from e

    async def generate(self, request: AIRequest) -> AIResponse:
        if not self._initialized:
            raise AIConnectionError("Gemini client is not initialized. Call initialize() first.")

        try:
            generation_config = GenerationConfig(
                temperature=request.temperature,
                max_output_tokens=request.max_tokens,
                candidate_count=1,
            )

            response = await self._model.generate_content_async(
                contents=request.prompt,
                generation_config=generation_config,
            )

            response_text = ""
            if response.candidates and len(response.candidates) > 0:
                candidate = response.candidates[0]
                if candidate.content and candidate.content.parts:
                    response_text = "".join(
                        part.text for part in candidate.content.parts if hasattr(part, 'text')
                    )

            return AIResponse(
                response_text=response_text,
                provider="gemini",
                metadata={
                    "model": self._model_name,
                    "finish_reason": str(candidate.finish_reason) if response.candidates else None,
                },
            )
        except Exception as e:
            error_msg = str(e).lower()
            # Klasifikasikan berdasarkan kata kunci dalam pesan error
            if any(kw in error_msg for kw in ("authentication", "api key", "unauthorized", "invalid key")):
                raise AIAuthenticationError(f"Authentication failed: {str(e)}") from e
            elif "rate limit" in error_msg or "quota" in error_msg:
                raise AIRateLimitError(f"Rate limit exceeded: {str(e)}") from e
            elif "timeout" in error_msg or "timed out" in error_msg:
                raise AITimeoutError(f"Request timed out: {str(e)}") from e
            elif "connection" in error_msg or "network" in error_msg or "unreachable" in error_msg:
                raise AIConnectionError(f"Connection error: {str(e)}") from e
            else:
                raise AIResponseError(f"Gemini API error: {str(e)}") from e

    async def health_check(self) -> bool:
        if not self._initialized:
            return False
        try:
            request = AIRequest(prompt="Ping", max_tokens=5)
            response = await self.generate(request)
            return bool(response.response_text)
        except Exception:
            return False

    async def close(self) -> None:
        pass