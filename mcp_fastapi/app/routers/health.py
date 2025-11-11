"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", summary="Simple health probe.")
async def health_check() -> dict[str, str]:
    """Return service status for probes."""
    return {"status": "ok"}

