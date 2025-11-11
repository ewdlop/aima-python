"""FastAPI entrypoint for the AIMA Online server."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from gradio.routes import mount_gradio_app

from .routers import aima, health, hf
from .settings import Settings, get_settings
from .ui import build_gradio_app


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = settings or get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        summary="AIMA Online API powered by FastAPI.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)
    app.include_router(aima.router)
    app.include_router(hf.router)

    return app


app = create_app()
mount_gradio_app(app, build_gradio_app(), path="/gradio")


@app.get("/", include_in_schema=False)
async def root_redirect() -> RedirectResponse:
    """Redirect root to the Gradio interface."""
    return RedirectResponse(url="/gradio")