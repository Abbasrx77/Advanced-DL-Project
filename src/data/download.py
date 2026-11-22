"""Download and verify the EuroSAT RGB dataset."""

from __future__ import annotations

from pathlib import Path


def download_eurosat(dest_dir: Path) -> Path:
    """Download and extract EuroSAT RGB into ``dest_dir``.

    Args:
        dest_dir: Destination directory (normally ``paths.data`` from the config).

    Returns:
        Path to the extracted dataset root (one sub-directory per class).
    """
    raise NotImplementedError("data.download : à implémenter")


def verify_dataset(root: Path) -> dict[str, int]:
    """Check that the dataset is complete and readable.

    Args:
        root: Dataset root returned by :func:`download_eurosat`.

    Returns:
        Number of images per class name.
    """
    raise NotImplementedError("data.download : à implémenter")
