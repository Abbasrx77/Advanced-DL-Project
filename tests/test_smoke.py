"""Smoke tests: every module imports, classes and config are consistent."""

from __future__ import annotations

import importlib
import pkgutil

import pytest

import src
from src.config import load_config
from src.data.classes import CLASS_TO_IDX, CLASSES, IDX_TO_CLASS, NUM_CLASSES

MODULES = sorted(m.name for m in pkgutil.walk_packages(src.__path__, prefix="src."))


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module: str) -> None:
    importlib.import_module(module)


def test_expected_modules_present() -> None:
    for package in ("data", "baseline", "dl", "generative", "rag", "tools", "app"):
        assert f"src.{package}" in MODULES


def test_classes() -> None:
    assert NUM_CLASSES == 10
    assert CLASSES == (
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
    for idx, name in enumerate(CLASSES):
        assert CLASS_TO_IDX[name] == idx
        assert IDX_TO_CLASS[idx] == name


def test_config_loads() -> None:
    config = load_config()
    assert config["seed"] == 42
    assert config["image_size"] == 64
    for key in ("data", "splits", "models", "reports", "knowledge_base"):
        assert key in config["paths"]
    for section in ("baseline", "dl", "generative", "rag"):
        assert section in config
