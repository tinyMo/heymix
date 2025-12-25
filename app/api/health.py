"""Health check endpoints."""
from fastapi import APIRouter

from app.config import get_settings

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", summary="Health check")
async def read_health() -> dict[str, str]:
    """Return basic application health information."""

    settings = get_settings()
    return {
        "status": "ok",
        "environment": settings.environment,
        "service": settings.app_name,
    }
