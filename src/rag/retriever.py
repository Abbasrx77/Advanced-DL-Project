"""Retriever over the persisted vector store."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from langchain_core.retrievers import BaseRetriever


def get_retriever(config: dict[str, Any]) -> BaseRetriever:
    """Load the vector store and return a LangChain retriever.

    Args:
        config: Project configuration.

    Returns:
        A retriever returning the most relevant chunks for a query.
    """
    raise NotImplementedError("rag.retriever : à implémenter")
