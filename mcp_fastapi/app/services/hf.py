"""Helpers for interacting with Hugging Face services."""

from __future__ import annotations

from functools import lru_cache
from typing import Any

from huggingface_hub import HfApi, InferenceClient
from huggingface_hub.utils import HfHubHTTPError

from ..schemas import (
    HFSpaceDeploymentResult,
    HFTextGenerationRequest,
    HFTextGenerationResponse,
)
from ..settings import Settings, get_settings


class MissingHFConfigurationError(RuntimeError):
    """Raised when required Hugging Face configuration is missing."""


@lru_cache
def _get_inference_client(
    model_id: str | None, api_url: str | None, token: str | None
) -> InferenceClient:
    """Return a cached inference client."""
    return InferenceClient(
        model=model_id,
        token=token,
        endpoint_url=api_url,
    )


def get_inference_client(
    settings: Settings, model_id: str | None = None, api_url: str | None = None
) -> InferenceClient:
    """Create an inference client using configuration or overrides."""
    token = settings.get_hf_token()
    client_model = model_id or settings.hf_inference_model
    client_api_url = api_url or settings.hf_inference_api_url

    if not client_model and not client_api_url:
        raise MissingHFConfigurationError(
            "必須設定 MCP_HF_INFERENCE_MODEL 或 MCP_HF_INFERENCE_API_URL。"
        )

    return _get_inference_client(client_model, client_api_url, token)


def run_text_generation(
    payload: HFTextGenerationRequest,
    settings: Settings | None = None,
) -> HFTextGenerationResponse:
    """Execute text generation via Hugging Face Inference API."""
    settings = settings or get_settings()
    client = get_inference_client(
        settings=settings,
        model_id=payload.model,
        api_url=payload.inference_api_url,
    )

    try:
        raw_result: Any = client.text_generation(
            payload.prompt,
            max_new_tokens=payload.max_new_tokens,
            temperature=payload.temperature,
            top_p=payload.top_p,
            stop_sequences=payload.stop_sequences,
            repetition_penalty=payload.repetition_penalty,
            do_sample=payload.do_sample,
            return_full_text=payload.return_full_text,
        )
    except HfHubHTTPError as exc:  # pragma: no cover - network error path
        raise RuntimeError(f"Hugging Face 推論呼叫失敗：{exc}") from exc

    if isinstance(raw_result, dict):
        text = raw_result.get("generated_text") or raw_result.get("text", "")
    else:
        text = str(raw_result)

    return HFTextGenerationResponse(
        model=client.model or "custom-endpoint",
        content=text,
        raw=raw_result,
    )


def deploy_space(
    repo_id: str,
    settings: Settings | None = None,
    space_sdk: str | None = None,
    space_hardware: str | None = None,
    private: bool | None = None,
    update_only: bool = False,
) -> HFSpaceDeploymentResult:
    """Create or update a Hugging Face Space."""
    settings = settings or get_settings()
    token = settings.get_hf_token()
    if not token:
        raise MissingHFConfigurationError("必須提供 MCP_HF_API_TOKEN 以呼叫 Hugging Face API。")

    api = HfApi(token=token)
    actual_sdk = space_sdk or settings.hf_space_sdk
    actual_hardware = space_hardware or settings.hf_space_hardware

    if update_only:
        try:
            space_info = api.repo_info(repo_id=repo_id, repo_type="space")
        except HfHubHTTPError as exc:
            if getattr(exc, "response", None) and getattr(exc.response, "status_code", None) == 404:
                raise MissingHFConfigurationError(
                    f"Space {repo_id} 不存在，若要自動建立請將 update_only 設為 false。"
                ) from exc
            raise
    else:
        space_info = api.create_repo(
            repo_id=repo_id,
            repo_type="space",
            space_sdk=actual_sdk,
            space_hardware=actual_hardware,
            exist_ok=True,
            private=private,
        )

    return HFSpaceDeploymentResult(
        repo_id=space_info.repo_id,
        url=space_info.url,
        space_sdk=actual_sdk,
        space_hardware=actual_hardware,
        private=space_info.private,
    )

