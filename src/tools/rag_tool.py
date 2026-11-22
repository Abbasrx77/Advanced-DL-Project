"""Knowledge base question tool for the orchestrator."""

from __future__ import annotations

from src.interfaces import RagAnswer


def ask_knowledge_base(question: str, predicted_label: str | None = None) -> RagAnswer:
    """Answer a question from the knowledge base.

    Args:
        question: User question.
        predicted_label: Class predicted for the user's image, if any.

    Returns:
        RAG answer with sources.
    """
    raise NotImplementedError("tools.rag_tool : à implémenter")
