"""EuroSAT classes: single source of truth for class names and indices.

The order is the official EuroSAT order. Never redefine this list elsewhere.
"""

from __future__ import annotations

CLASSES: tuple[str, ...] = (
    "AnnualCrop",
    "Forest",
    "HerbaceousVegetation",
    "Highway",
    "Industrial",
    "Pasture",
    "PermanentCrop",
    "Residential",
    "River",
    "SeaLake",
)

NUM_CLASSES: int = len(CLASSES)

CLASS_TO_IDX: dict[str, int] = {name: idx for idx, name in enumerate(CLASSES)}
IDX_TO_CLASS: dict[int, str] = dict(enumerate(CLASSES))
