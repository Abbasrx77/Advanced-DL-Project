"""Train the baseline classifier on the train split (validation split for model selection)."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def train_baseline(config: dict[str, Any]) -> Path:
    """Extract features, fit the classifier and save it.

    Args:
        config: Project configuration.

    Returns:
        Path to the saved model.
    """
    raise NotImplementedError("baseline.train : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.baseline.train``."""
    raise NotImplementedError("baseline.train : à implémenter")


if __name__ == "__main__":
    main()
