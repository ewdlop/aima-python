"""Application configuration."""

from __future__ import annotations

from functools import lru_cache
from typing import Sequence

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Environment-driven application settings."""

    app_name: str = "AIMA Online Server"
    version: str = "0.1.0"
    allowed_origins: Sequence[str] = ("*",)
    default_model: str = "demo-mcp-model"
    hf_api_token: SecretStr | None = None
    hf_inference_model: str | None = None
    hf_inference_api_url: str | None = None
    hf_space_repo: str | None = None
    hf_space_sdk: str = "docker"
    hf_space_hardware: str = "cpu-basic"

    class Config:
        env_prefix = "MCP_"

    def get_hf_token(self) -> str | None:
        """Return the plain Hugging Face token if configured."""
        return self.hf_api_token.get_secret_value() if self.hf_api_token else None


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()

