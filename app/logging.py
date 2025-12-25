"""Logging configuration utilities."""
import logging
import logging.config

from .config import get_settings


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        }
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        }
    },
    "loggers": {
        "": {
            "handlers": ["default"],
            "level": "INFO",
        }
    },
}


def configure_logging() -> None:
    """Configure application-wide logging."""

    settings = get_settings()
    config = LOGGING_CONFIG.copy()
    config["loggers"][""]["level"] = settings.log_level.upper()
    logging.config.dictConfig(config)
    logging.getLogger(__name__).debug("Logging configured with level %s", settings.log_level)
