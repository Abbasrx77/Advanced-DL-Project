"""Train the deep learning classifier."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def train_model(config: dict[str, Any]) -> Path:
    """Train on the train split, select on the validation split and save the best checkpoint.

    Args:
        config: Project configuration.

    Returns:
        Path to the saved checkpoint.
    """
    raise NotImplementedError("dl.train : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.dl.train``."""
    raise NotImplementedError("dl.train : à implémenter")


if __name__ == "__main__":
    main()
