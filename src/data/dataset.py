"""PyTorch datasets and data loaders built from the frozen splits."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any

from PIL import Image

if TYPE_CHECKING:
    import torch
    from torch.utils.data import DataLoader


class EuroSATDataset:
    """Dataset over one split, compatible with ``torch.utils.data.DataLoader``.

    Args:
        data_root: Dataset root (one sub-directory per class).
        samples: ``(relative_image_path, class_name)`` pairs for this split.
        transform: Transform from ``src/data/transforms.py``.
    """

    def __init__(
        self,
        data_root: Path,
        samples: list[tuple[str, str]],
        transform: Callable[[Image.Image], torch.Tensor] | None = None,
    ) -> None:
        raise NotImplementedError("data.dataset : à implémenter")

    def __len__(self) -> int:
        """Return the number of samples."""
        raise NotImplementedError("data.dataset : à implémenter")

    def __getitem__(self, index: int) -> tuple[torch.Tensor, int]:
        """Return ``(image_tensor, class_index)`` for sample ``index``."""
        raise NotImplementedError("data.dataset : à implémenter")


def build_dataloaders(config: dict[str, Any]) -> dict[str, DataLoader]:
    """Build one data loader per split from the config.

    Args:
        config: Project configuration.

    Returns:
        Data loader per split name (``train``, ``val``, ``test``).
    """
    raise NotImplementedError("data.dataset : à implémenter")
