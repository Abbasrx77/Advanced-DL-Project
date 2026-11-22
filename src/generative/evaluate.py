"""Evaluate generated images and write metrics to ``reports/``."""

from __future__ import annotations

from typing import Any

from src.interfaces import Classifier, Generator


def evaluate_generator(
    generator: Generator, classifier: Classifier, config: dict[str, Any]
) -> dict[str, float]:
    """Compute quality metrics of the generator.

    Args:
        generator: Trained generator.
        classifier: Trained classifier, used to check that generated images match their label.
        config: Project configuration.

    Returns:
        Metric name to value.
    """
    raise NotImplementedError("generative.evaluate : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.generative.evaluate``."""
    raise NotImplementedError("generative.evaluate : à implémenter")


if __name__ == "__main__":
    main()
