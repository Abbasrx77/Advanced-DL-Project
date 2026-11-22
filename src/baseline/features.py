"""Hand-crafted feature extraction (scikit-image)."""

from __future__ import annotations

from typing import Any

import numpy as np
from PIL import Image


def extract_features(image: Image.Image, config: dict[str, Any]) -> np.ndarray:
    """Compute the feature vector of one image.

    Args:
        image: PIL RGB image.
        config: ``baseline`` section of the config (feature parameters).

    Returns:
        1-D feature vector.
    """
    raise NotImplementedError("baseline.features : à implémenter")


def extract_features_batch(images: list[Image.Image], config: dict[str, Any]) -> np.ndarray:
    """Compute features for a list of images.

    Args:
        images: PIL RGB images.
        config: ``baseline`` section of the config.

    Returns:
        Feature matrix of shape ``(n_images, n_features)``.
    """
    raise NotImplementedError("baseline.features : à implémenter")
