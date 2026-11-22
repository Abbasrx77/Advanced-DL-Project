"""Train the generative model."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def train_generative_model(config: dict[str, Any]) -> Path:
    """Train on the train split and save the checkpoint.

    Args:
        config: Project configuration.

    Returns:
        Path to the saved checkpoint.
    """
    raise NotImplementedError("generative.train : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.generative.train``."""
    raise NotImplementedError("generative.train : à implémenter")


if __name__ == "__main__":
    main()
