"""FastAPI application entrypoint.

Configures CORS, includes routers, and exposes a healthcheck endpoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .deps import get_settings
from .routers import auth as auth_router

# Import models so Alembic can discover metadata
from . import models  # noqa: F401


def create_app() -> FastAPI:
    app = FastAPI(title="AdNavi API")

    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router.router)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()



