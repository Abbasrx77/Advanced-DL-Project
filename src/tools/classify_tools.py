"""Classification tools for the orchestrator."""

from __future__ import annotations

from PIL import Image

from src.interfaces import Prediction


def classify_baseline(image: Image.Image) -> Prediction:
    """Classify an image with the baseline model.

    Args:
        image: PIL RGB image.

    Returns:
        Baseline prediction.
    """
    raise NotImplementedError("tools.classify_tools : à implémenter")


def classify_dl(image: Image.Image) -> Prediction:
    """Classify an image with the deep learning model.

    Args:
        image: PIL RGB image.

    Returns:
        Deep learning prediction.
    """
    raise NotImplementedError("tools.classify_tools : à implémenter")
