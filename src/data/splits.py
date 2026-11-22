"""Create, save and load the frozen train/val/test splits.

Splits are computed once, saved in ``splits/`` and committed. The test split is used only
for the final evaluation.
"""

from __future__ import annotations

from pathlib import Path


def make_splits(
    data_root: Path, ratios: dict[str, float], seed: int
) -> dict[str, list[tuple[str, str]]]:
    """Split the dataset into train/val/test.

    Args:
        data_root: Dataset root (one sub-directory per class).
        ratios: Fraction per split name (``train``, ``val``, ``test``), from the config.
        seed: Random seed, from the config.

    Returns:
        For each split name, a list of ``(relative_image_path, class_name)`` pairs.
    """
    raise NotImplementedError("data.splits : à implémenter")


def save_splits(splits: dict[str, list[tuple[str, str]]], out_dir: Path) -> None:
    """Write the splits to ``out_dir`` (one file per split).

    Args:
        splits: Output of :func:`make_splits`.
        out_dir: Destination directory (normally ``paths.splits``).
    """
    raise NotImplementedError("data.splits : à implémenter")


def load_splits(split_dir: Path) -> dict[str, list[tuple[str, str]]]:
    """Read the splits saved by :func:`save_splits`.

    Args:
        split_dir: Directory containing the split files.

    Returns:
        Same structure as :func:`make_splits`.
    """
    raise NotImplementedError("data.splits : à implémenter")
