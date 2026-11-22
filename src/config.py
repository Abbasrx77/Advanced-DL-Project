"""Load the project configuration (``configs/default.yaml``)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "configs" / "default.yaml"


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    """Load a YAML configuration file.

    Args:
        path: Path to the YAML file. Relative paths are resolved from the project root.
            Defaults to ``configs/default.yaml``.

    Returns:
        The configuration as a nested dictionary.
    """
    config_path = Path(path) if path is not None else DEFAULT_CONFIG_PATH
    if not config_path.is_absolute():
        config_path = PROJECT_ROOT / config_path
    with config_path.open(encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        raise ValueError(f"Invalid config file (expected a mapping): {config_path}")
    return config


def resolve_path(config: dict[str, Any], key: str) -> Path:
    """Return the absolute path for an entry of the ``paths`` section.

    Args:
        config: Configuration returned by :func:`load_config`.
        key: Key in ``config["paths"]`` (e.g. ``"data"``, ``"models"``).

    Returns:
        Absolute path, resolved from the project root.
    """
    return PROJECT_ROOT / config["paths"][key]
