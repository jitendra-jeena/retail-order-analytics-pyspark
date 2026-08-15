"""
Application logging utility.

Provides console logging, rotating file logging, configurable log levels,
UTF-8 encoded files, exception logging, automatic directory creation,
duplicate handler prevention, and a reusable get_logger() function.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "application.log"
DEFAULT_MAX_BYTES = 10 * 1024 * 1024
DEFAULT_BACKUP_COUNT = 5

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


def _get_log_level(level: str) -> int:
    """Convert a log-level string to its logging constant.

    Args:
        level: Case-insensitive level string (e.g. "INFO").

    Returns:
        The corresponding logging constant (e.g. logging.INFO).

    Raises:
        ValueError: If level is not one of VALID_LOG_LEVELS.
    """
    normalized = level.strip().upper()
    if normalized not in VALID_LOG_LEVELS:
        raise ValueError(
            f"Invalid log level: '{level}'. "
            f"Expected one of: {', '.join(sorted(VALID_LOG_LEVELS))}."
        )
    return getattr(logging, normalized)


def _create_formatter() -> logging.Formatter:
    """Create the standard application log formatter."""
    return logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)


def get_logger(
    name: Optional[str] = None, log_level: str = DEFAULT_LOG_LEVEL,
    log_dir: str = DEFAULT_LOG_DIR, log_file: str = DEFAULT_LOG_FILE,
    max_bytes: int = DEFAULT_MAX_BYTES, backup_count: int = DEFAULT_BACKUP_COUNT,
) -> logging.Logger:
    """Create or retrieve a configured application logger.

    Returns the same logger instance if already configured, preventing
    duplicate handlers. Sets propagate=False to avoid double-logging
    through parent loggers.

    Args:
        name: Logger name, typically __name__. Defaults to "retail_analytics".
        log_level: Level for both handlers. One of VALID_LOG_LEVELS.
        log_dir: Directory for log files. Created if missing.
        log_file: Name of the log file.
        max_bytes: Max size in bytes before rotation.
        backup_count: Number of rotated files to keep.

    Returns:
        Configured logger with console and rotating file handlers.

    Raises:
        ValueError: If log_level is invalid.

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("Started")
    """
    logger_name = name or "retail_analytics"
    logger = logging.getLogger(logger_name)

    if getattr(logger, "_configured", False):
        return logger

    level = _get_log_level(log_level)
    logger.setLevel(level)
    logger.propagate = False
    formatter = _create_formatter()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    Path(log_dir).mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        filename=Path(log_dir) / log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger._configured = True  # type: ignore[attr-defined]

    return logger


def configure_root_logger(log_level: str = DEFAULT_LOG_LEVEL, log_dir: str = DEFAULT_LOG_DIR, log_file: str = DEFAULT_LOG_FILE) -> logging.Logger:
    """Configure the root application logger with a fixed name.

    Convenience wrapper for entry-point scripts that need one global
    logger named "retail_analytics".

    Args:
        log_level: Level for both handlers.
        log_dir: Directory for log files.
        log_file: Name of the log file.

    Returns:
        The configured logger.
    """
    return get_logger(name="retail_analytics", log_level=log_level, log_dir=log_dir, log_file=log_file)
