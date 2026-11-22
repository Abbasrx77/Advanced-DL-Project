"""Load the knowledge base documents and build the vector store."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from langchain_core.documents import Document


def load_documents(raw_dir: Path) -> list[Document]:
    """Load the documents of ``knowledge_base/raw/`` (each one listed in ``sources.md``).

    Args:
        raw_dir: Directory containing the raw documents.

    Returns:
        Loaded documents with their source in the metadata.
    """
    raise NotImplementedError("rag.ingest : à implémenter")


def split_documents(documents: list[Document], config: dict[str, Any]) -> list[Document]:
    """Split documents into chunks.

    Args:
        documents: Output of :func:`load_documents`.
        config: ``rag`` section of the config (chunking parameters).

    Returns:
        Chunks, keeping the source metadata.
    """
    raise NotImplementedError("rag.ingest : à implémenter")


def build_vector_store(chunks: list[Document], config: dict[str, Any]) -> Path:
    """Embed the chunks with Ollama and persist the vector store.

    Args:
        chunks: Output of :func:`split_documents`.
        config: Project configuration.

    Returns:
        Path to the persisted vector store.
    """
    raise NotImplementedError("rag.ingest : à implémenter")


def main() -> None:
    """Command-line entry point: ``python -m src.rag.ingest``."""
    raise NotImplementedError("rag.ingest : à implémenter")


if __name__ == "__main__":
    main()
