"""Hugging Face integration endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.concurrency import run_in_threadpool

from ..schemas import (
    HFSpaceDeployRequest,
    HFSpaceDeploymentResult,
    HFTextGenerationRequest,
    HFTextGenerationResponse,
)
from ..services.hf import MissingHFConfigurationError, deploy_space, run_text_generation
from ..settings import Settings, get_settings

router = APIRouter(prefix="/hf", tags=["huggingface"])


@router.get(
    "/config",
    summary="檢視 Hugging Face 設定狀態。",
)
async def get_hf_config(settings: Settings = Depends(get_settings)) -> dict[str, str | None]:
    """Expose部分 Hugging Face 相關設定（不含密鑰）。"""
    return {
        "hf_space_repo": settings.hf_space_repo,
        "hf_space_sdk": settings.hf_space_sdk,
        "hf_space_hardware": settings.hf_space_hardware,
        "hf_inference_model": settings.hf_inference_model,
        "hf_inference_api_url": settings.hf_inference_api_url,
    }


@router.post(
    "/text-generation",
    response_model=HFTextGenerationResponse,
    summary="使用 Hugging Face Inference API 進行文字生成。",
)
async def text_generation(
    payload: HFTextGenerationRequest,
    settings: Settings = Depends(get_settings),
) -> HFTextGenerationResponse:
    """Proxy text generation requests to Hugging Face."""
    try:
        return await run_in_threadpool(run_text_generation, payload, settings)
    except MissingHFConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc


@router.post(
    "/spaces/deploy",
    response_model=HFSpaceDeploymentResult,
    summary="透過 Hugging Face API 建立或更新 Space。",
)
async def deploy_space_endpoint(
    payload: HFSpaceDeployRequest,
    settings: Settings = Depends(get_settings),
) -> HFSpaceDeploymentResult:
    """Create or update a Hugging Face Space using stored credentials."""
    repo_id = payload.repo_id or settings.hf_space_repo
    if not repo_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="必須提供 repo_id 或在環境變數 MCP_HF_SPACE_REPO 中設定預設值。",
        )

    try:
        return await run_in_threadpool(
            deploy_space,
            repo_id=repo_id,
            settings=settings,
            space_sdk=payload.space_sdk,
            space_hardware=payload.space_hardware,
            private=payload.private,
            update_only=payload.update_only,
        )
    except MissingHFConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

