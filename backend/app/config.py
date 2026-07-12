from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings."""
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Gemini API
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"   # default model

    # AI Provider
    ai_provider: str = "gemini"

    # CORS
    cors_origins: list[str] = ["http://localhost:5173"]

    # File upload validation
    max_upload_size: int = 20 * 1024 * 1024
    allowed_extensions: list[str] = [".pdf", ".docx", ".txt"]


@lru_cache()
def get_settings() -> Settings:
    return Settings()