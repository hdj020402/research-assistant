"""Markdown file writing utilities for Obsidian notes."""
import re
from pathlib import Path


def sanitize_filename(name: str, max_length: int = 80) -> str:
    """Convert a string to a safe filename, preserving readability."""
    # Remove characters not safe for filenames
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", name)
    # Replace multiple spaces/dashes with single
    name = re.sub(r"[\s_]+", "_", name.strip())
    name = re.sub(r"-+", "-", name)
    # Truncate
    if len(name) > max_length:
        name = name[:max_length].rstrip("_- ")
    return name


def write_markdown(path: Path, content: str) -> None:
    """Write content to a markdown file, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def append_markdown(path: Path, content: str) -> None:
    """Append content to an existing markdown file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
