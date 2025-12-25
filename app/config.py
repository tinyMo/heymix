"""Application settings and environment configuration."""
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application runtime settings loaded from environment variables."""

    app_name: str = Field(default="heymix", description="Application name")
    environment: str = Field(default="development", description="Deployment environment identifier")
    log_level: str = Field(default="INFO", description="Logging level for the application")
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_", env_file_encoding="utf-8", extra="ignore")


@lru_cache

def get_settings() -> Settings:
    """Return cached application settings instance."""

    return Settings()
