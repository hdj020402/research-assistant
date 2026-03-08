"""Unified Claude API client supporting haiku and opus models."""
import os
import anthropic
from typing import Optional


class ClaudeClient:
    def __init__(self, config: dict):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        base_url = os.environ.get("ANTHROPIC_BASE_URL")
        kwargs = {"api_key": api_key, "timeout": 120.0}
        if base_url:
            kwargs["base_url"] = base_url
        self.client = anthropic.Anthropic(**kwargs)
        self.haiku_model = config["claude"]["haiku_model"]
        self.opus_model = config["claude"]["opus_model"]
        self.max_tokens_haiku = config["claude"]["max_tokens_haiku"]
        self.max_tokens_opus = config["claude"]["max_tokens_opus"]

    def haiku(self, prompt: str, system: Optional[str] = None) -> str:
        """Call Claude Haiku for fast, lightweight tasks."""
        kwargs = {
            "model": self.haiku_model,
            "max_tokens": self.max_tokens_haiku,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system
        response = self.client.messages.create(**kwargs)
        return response.content[0].text

    def opus(self, prompt: str, system: Optional[str] = None) -> str:
        """Call Claude Opus for deep analysis tasks."""
        kwargs = {
            "model": self.opus_model,
            "max_tokens": self.max_tokens_opus,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system
        response = self.client.messages.create(**kwargs)
        return response.content[0].text
