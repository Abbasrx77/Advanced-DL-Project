"""Image generation with the trained model (implements ``interfaces.Generator``)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.interfaces import GenerationResult


class ConditionalGenerator:
    """Generative model loaded from a checkpoint.

    Args:
        checkpoint: Path to the saved checkpoint.
        config: Project configuration.
    """

    def __init__(self, checkpoint: Path, config: dict[str, Any]) -> None:
        raise NotImplementedError("generative.generate : à implémenter")

    def generate(self, label: str, n: int, seed: int) -> GenerationResult:
        """Generate ``n`` images of class ``label``.

        Args:
            label: EuroSAT class name.
            n: Number of images to generate.
            seed: Random seed (same seed, same images).

        Returns:
            Generated PIL RGB images, converted with ``src/data/transforms.py``.
        """
        raise NotImplementedError("generative.generate : à implémenter")
