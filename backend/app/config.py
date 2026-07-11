from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    gemini_api_key: str = ""
    cors_origins: list[str] = ["http://localhost:5173"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    return Settings()