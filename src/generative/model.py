"""Class-conditional generative model architecture (VAE, GAN or diffusion)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from torch import nn


def build_generative_model(config: dict[str, Any]) -> nn.Module:
    """Build the generative network.

    Args:
        config: ``generative`` section of the config (architecture parameters).

    Returns:
        A ``torch.nn.Module`` conditioned on the EuroSAT class index.
    """
    raise NotImplementedError("generative.model : à implémenter")
