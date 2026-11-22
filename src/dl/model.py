"""Deep learning classifier architecture."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import nn


def build_model(config: dict[str, Any]) -> nn.Module:
    """Build the classifier network.

    Args:
        config: ``dl`` section of the config (architecture parameters).

    Returns:
        A ``torch.nn.Module`` producing one logit per EuroSAT class.
    """
    raise NotImplementedError("dl.model : à implémenter")
