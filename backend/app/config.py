"""
Centralized configuration for the backend.
All settings are loaded from environment variables / .env file.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings."""

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Gemini API
    gemini_api_key: str = ""

    # CORS origins
    cors_origins: list[str] = ["http://localhost:5173"]

    # File upload validation
    max_upload_size: int = 20 * 1024 * 1024  # 20 MB
    allowed_extensions: list[str] = [".pdf", ".docx", ".txt"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    Returns a cached instance of Settings.
    This ensures the .env file is read only once.
    """
    return Settings()