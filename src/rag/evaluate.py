"""Evaluate the RAG system on a question set and write metrics to ``reports/``."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.interfaces import RagSystem


def evaluate_rag(rag: RagSystem, questions_path: Path, config: dict[str, Any]) -> dict[str, float]:
    """Run the question set through the RAG system and score the answers.

    Args:
        rag: RAG system to evaluate.
        questions_path: File with the evaluation questions and expected answers or sources.
        config: Project configuration.

    Returns:
        Metric name to value.
    """
    raise NotImplementedError("rag.evaluate : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.rag.evaluate``."""
    raise NotImplementedError("rag.evaluate : à implémenter")


if __name__ == "__main__":
    main()
