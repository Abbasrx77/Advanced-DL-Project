"""Evaluate the deep learning classifier and write metrics to ``reports/``."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def evaluate_model(
    checkpoint: Path, config: dict[str, Any], split: str = "val"
) -> dict[str, float]:
    """Compute metrics of a checkpoint on one split.

    Args:
        checkpoint: Path returned by ``train_model``.
        config: Project configuration.
        split: Split to evaluate on. ``"test"`` only for the final evaluation.

    Returns:
        Metric name to value.
    """
    raise NotImplementedError("dl.evaluate : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.dl.evaluate``."""
    raise NotImplementedError("dl.evaluate : à implémenter")


if __name__ == "__main__":
    main()
