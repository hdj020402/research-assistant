"""YAML config loader with environment variable secrets injection."""
import os
import yaml
from pathlib import Path


def load_config(config_path: str = "config.yml") -> dict:
    """Load config.yml and inject secrets from environment variables."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.full_load(f)
    return config


def get_secret(key: str, required: bool = True) -> str:
    """Read a secret from environment variables."""
    value = os.environ.get(key)
    if required and not value:
        raise ValueError(f"Required secret '{key}' not found in environment variables")
    return value or ""
