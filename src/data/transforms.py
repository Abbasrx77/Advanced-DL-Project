"""Image preprocessing shared by training, generated images and the app.

Every component must use these functions instead of defining its own preprocessing.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from PIL import Image

if TYPE_CHECKING:
    import torch


def load_rgb(path: str) -> Image.Image:
    """Open an image file as a PIL RGB image.

    Args:
        path: Path to the image file.

    Returns:
        The image in RGB mode.
    """
    raise NotImplementedError("data.transforms : à implémenter")


def get_train_transform(image_size: int) -> Callable[[Image.Image], torch.Tensor]:
    """Return the training transform (may include data augmentation).

    Args:
        image_size: Target side length in pixels (``image_size`` in the config).

    Returns:
        A callable mapping a PIL RGB image to a model input tensor.
    """
    raise NotImplementedError("data.transforms : à implémenter")


def get_eval_transform(image_size: int) -> Callable[[Image.Image], torch.Tensor]:
    """Return the deterministic transform used for evaluation, generation checks and the app.

    Args:
        image_size: Target side length in pixels (``image_size`` in the config).

    Returns:
        A callable mapping a PIL RGB image to a model input tensor.
    """
    raise NotImplementedError("data.transforms : à implémenter")


def tensor_to_pil(tensor: torch.Tensor) -> Image.Image:
    """Convert a model output tensor back to a PIL RGB image (inverse of normalisation).

    Args:
        tensor: Image tensor of shape ``(3, H, W)``.

    Returns:
        The corresponding PIL RGB image.
    """
    raise NotImplementedError("data.transforms : à implémenter")
