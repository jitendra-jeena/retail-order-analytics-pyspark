"""
Path utilities for the Retail Analytics project.

Keeps project data paths consistent and avoids hard-coded
path construction throughout the application.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DATA_DIR = DATA_DIR / "output"
CHECKPOINT_DIR = DATA_DIR / "checkpoints"
LOG_DIR = PROJECT_ROOT / "logs"


def get_raw_data_path(dataset: str) -> Path:
    """Return the path for a raw dataset."""
    return RAW_DATA_DIR / dataset


def get_processed_data_path(dataset: str) -> Path:
    """Return the path for a processed dataset."""
    return PROCESSED_DATA_DIR / dataset


def get_output_data_path(dataset: str) -> Path:
    """Return the path for an output dataset."""
    return OUTPUT_DATA_DIR / dataset
