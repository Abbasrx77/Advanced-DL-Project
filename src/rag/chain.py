"""RAG chain answering questions from the knowledge base (implements ``interfaces.RagSystem``)."""

from __future__ import annotations

from typing import Any

from src.interfaces import RagAnswer


class RagPipeline:
    """Retriever + local LLM (Ollama).

    Args:
        config: Project configuration.
    """

    def __init__(self, config: dict[str, Any]) -> None:
        raise NotImplementedError("rag.chain : à implémenter")

    def ask(self, question: str, predicted_label: str | None = None) -> RagAnswer:
        """Answer a question using only the retrieved documents.

        Args:
            question: User question.
            predicted_label: Class predicted for the user's image, if any.

        Returns:
            Answer, cited sources, and whether the evidence was insufficient.
        """
        raise NotImplementedError("rag.chain : à implémenter")
