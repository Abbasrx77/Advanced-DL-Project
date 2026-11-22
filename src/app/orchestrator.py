"""Orchestrator: routes a user request to the right tool(s) and assembles the response."""

from __future__ import annotations

from dataclasses import dataclass, field

from PIL import Image

from src.interfaces import GenerationResult, Prediction, RagAnswer


@dataclass
class AssistantResponse:
    """Response returned to the app.

    Attributes:
        text: Message shown to the user.
        tools_used: Names of the tools called, in order.
        predictions: Classifier outputs, if any.
        generation: Generation output, if any.
        rag_answer: RAG output, if any.
    """

    text: str
    tools_used: list[str] = field(default_factory=list)
    predictions: list[Prediction] = field(default_factory=list)
    generation: GenerationResult | None = None
    rag_answer: RagAnswer | None = None


class Orchestrator:
    """Entry point used by the app for every user request."""

    def handle(self, message: str, image: Image.Image | None = None) -> AssistantResponse:
        """Decide which tools to call for this request, call them and build the response.

        Args:
            message: User message.
            image: Optional PIL RGB image uploaded by the user.

        Returns:
            Assembled response.
        """
        raise NotImplementedError("app.orchestrator : à implémenter")
