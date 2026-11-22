"""Inference with the trained baseline (implements ``interfaces.Classifier``)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image

from src.interfaces import Prediction


class BaselineClassifier:
    """Baseline classifier loaded from disk.

    Args:
        model_path: Path to the saved model.
        config: Project configuration.
    """

    def __init__(self, model_path: Path, config: dict[str, Any]) -> None:
        raise NotImplementedError("baseline.predict : à implémenter")

    def predict(self, image: Image.Image) -> Prediction:
        """Classify one PIL RGB image.

        Args:
            image: PIL RGB image.

        Returns:
            Prediction with ``model="baseline"``.
        """
        raise NotImplementedError("baseline.predict : à implémenter")
