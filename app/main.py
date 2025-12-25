"""FastAPI application entrypoint."""
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app import logging as app_logging
from app.api import health
from app.config import get_settings


@asynccontextmanager
def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan context manager."""

    app_logging.configure_logging()
    yield


def create_application() -> FastAPI:
    """Create and configure the FastAPI application instance."""

    settings = get_settings()
    application = FastAPI(title=settings.app_name, lifespan=lifespan)
    application.include_router(health.router)
    return application


app = create_application()
