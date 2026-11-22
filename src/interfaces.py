"""Contracts shared between components.

Conventions:
- Images enter every component as ``PIL.Image.Image`` in RGB mode.
- Every image transformation goes through ``src/data/transforms.py``, so that training,
  generated images and the app all use exactly the same preprocessing.
- Labels are EuroSAT class names as defined in ``src/data/classes.py`` (single source of truth).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from PIL import Image


@dataclass
class Prediction:
    """Output of a classifier.

    Attributes:
        model: Identifier of the model that produced the prediction (e.g. ``"baseline"``).
        label: Predicted class name.
        confidence: Probability of the predicted class, in [0, 1].
        probs: Probability for each class name.
    """

    model: str
    label: str
    confidence: float
    probs: dict[str, float]


@dataclass
class GenerationResult:
    """Output of a generative model.

    Attributes:
        images: Generated images (PIL, RGB).
        prompt: Request that produced the images.
        label: Class name the images were conditioned on.
        seed: Random seed used for generation.
    """

    images: list[Image.Image]
    prompt: str
    label: str
    seed: int


@dataclass
class RagAnswer:
    """Output of the RAG system.

    Attributes:
        answer: Generated answer.
        sources: Identifiers of the documents used to answer.
        insufficient_evidence: True when the retrieved documents do not support an answer.
    """

    answer: str
    sources: list[str]
    insufficient_evidence: bool


@runtime_checkable
class Classifier(Protocol):
    """Any image classifier (baseline or deep learning)."""

    def predict(self, image: Image.Image) -> Prediction:
        """Classify one RGB image."""
        ...


@runtime_checkable
class Generator(Protocol):
    """Any class-conditional image generator."""

    def generate(self, label: str, n: int, seed: int) -> GenerationResult:
        """Generate ``n`` images of class ``label`` with a fixed ``seed``."""
        ...


@runtime_checkable
class RagSystem(Protocol):
    """Question answering over the knowledge base."""

    def ask(self, question: str, predicted_label: str | None = None) -> RagAnswer:
        """Answer ``question``, optionally using a predicted class as context."""
        ...
