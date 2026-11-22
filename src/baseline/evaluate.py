"""Evaluate the baseline classifier and write metrics to ``reports/``."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def evaluate_baseline(
    model_path: Path, config: dict[str, Any], split: str = "val"
) -> dict[str, float]:
    """Compute metrics of a saved baseline model on one split.

    Args:
        model_path: Path returned by ``train_baseline``.
        config: Project configuration.
        split: Split to evaluate on. ``"test"`` only for the final evaluation.

    Returns:
        Metric name to value.
    """
    raise NotImplementedError("baseline.evaluate : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.baseline.evaluate``."""
    raise NotImplementedError("baseline.evaluate : à implémenter")


if __name__ == "__main__":
    main()
