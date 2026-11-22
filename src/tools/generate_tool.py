"""Image generation tool for the orchestrator."""

from __future__ import annotations

from src.interfaces import GenerationResult


def generate_images(label: str, n: int, seed: int) -> GenerationResult:
    """Generate synthetic images of a EuroSAT class.

    Args:
        label: EuroSAT class name.
        n: Number of images.
        seed: Random seed.

    Returns:
        Generation result.
    """
    raise NotImplementedError("tools.generate_tool : à implémenter")
