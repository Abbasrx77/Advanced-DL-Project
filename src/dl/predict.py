"""Inference with the trained deep learning model (implements ``interfaces.Classifier``)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image

from src.interfaces import Prediction


class DLClassifier:
    """Deep learning classifier loaded from a checkpoint.

    Args:
        checkpoint: Path to the saved checkpoint.
        config: Project configuration.
    """

    def __init__(self, checkpoint: Path, config: dict[str, Any]) -> None:
        raise NotImplementedError("dl.predict : à implémenter")

    def predict(self, image: Image.Image) -> Prediction:
        """Classify one PIL RGB image.

        Args:
            image: PIL RGB image.

        Returns:
            Prediction with ``model="dl"``.
        """
        raise NotImplementedError("dl.predict : à implémenter")
