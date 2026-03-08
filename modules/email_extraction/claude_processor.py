"""Claude Haiku processor: translate abstracts, generate tags, score relevance."""
import json
import logging
import re
from dataclasses import dataclass
from typing import Optional
from shared.claude_client import ClaudeClient
from shared.rate_limiter import RateLimiter

log = logging.getLogger(__name__)
_rate_limiter = RateLimiter(calls_per_second=0.5)

SYSTEM_PROMPT = (
    "You are an expert AI chemistry researcher. "
    "Your task is to analyze academic paper abstracts and return structured JSON responses. "
    "Always respond with valid JSON only, no markdown code blocks."
)


@dataclass
class ProcessedArticle:
    title: str
    journal: str
    doi: str
    url: str
    abstract_en: str
    abstract_zh: str
    tags: list[str]
    ai_relevance: int  # 1-5
    title_zh: str = ""
    highlights: str = ""
    pub_date: str = ""
    authors: str = ""


def process_article(
    title: str,
    abstract: str,
    journal: str,
    doi: str,
    url: str,
    authors: str,
    pub_date: str,
    claude: ClaudeClient,
    tldr: str = "",
) -> ProcessedArticle:
    """
    Use Claude Haiku to:
    1. Translate abstract to Chinese
    2. Generate 3-5 topic tags
    3. Score AI-for-Chemistry relevance (1-5)
    """
    _rate_limiter.wait()

    if tldr:
        highlights_instruction = (
            '- "highlights": Translate the TLDR below to Chinese (1-2 sentences), '
            'followed by a blank line and keywords in this format: '
            '"**关键词**: 词1、词2、词3"'
        )
        tldr_section = f"\nTLDR: {tldr}"
    else:
        highlights_instruction = (
            '- "highlights": 1-2 sentence Chinese summary of key contributions/highlights, '
            'followed by a blank line and keywords in this format: '
            '"**关键词**: 词1、词2、词3"'
        )
        tldr_section = ""

    prompt = f"""Analyze this chemistry paper abstract and return a JSON object with these exact keys:
- "title_zh": Chinese translation of the paper title
- "abstract_zh": Chinese translation of the abstract (comprehensive, 100-200 Chinese characters)
{highlights_instruction}
- "tags": array of 3-5 lowercase English topic tags (e.g. ["machine-learning", "catalyst-design"])
- "ai_relevance": integer 1-5 scoring relevance to "AI for Chemistry" research
  (1=no AI, 2=minor computational, 3=ML/DL applied, 4=significant AI contribution, 5=core AI+Chemistry)

Paper title: {title}
Journal: {journal}
Abstract: {abstract if abstract else "No abstract available."}{tldr_section}

Respond with JSON only."""

    result = claude.haiku(prompt, system=SYSTEM_PROMPT)

    # Parse JSON response
    abstract_zh, tags, ai_relevance, title_zh, highlights = _parse_response(result, abstract)

    # Retry once on parse failure
    if abstract_zh == "翻译失败":
        log.warning(f"Claude parse failed, retrying: {title[:50]}")
        _rate_limiter.wait()
        result = claude.haiku(prompt, system=SYSTEM_PROMPT)
        abstract_zh, tags, ai_relevance, title_zh, highlights = _parse_response(result, abstract)

    return ProcessedArticle(
        title=title,
        journal=journal,
        doi=doi,
        url=url,
        abstract_en=abstract,
        abstract_zh=abstract_zh,
        tags=tags,
        ai_relevance=ai_relevance,
        title_zh=title_zh,
        highlights=highlights,
        pub_date=pub_date,
        authors=authors,
    )


def _parse_response(
    response: str, original_abstract: str
) -> tuple[str, list[str], int, str, str]:
    """Parse Claude's JSON response, with fallback values on failure."""
    try:
        # Strip markdown code blocks if present
        cleaned = re.sub(r"```(?:json)?\s*|\s*```", "", response.strip())
        data = json.loads(cleaned)
        abstract_zh = data.get("abstract_zh", "翻译失败")
        tags = data.get("tags", [])
        if not isinstance(tags, list):
            tags = []
        tags = [str(t).lower().strip() for t in tags[:5]]
        ai_relevance = int(data.get("ai_relevance", 1))
        ai_relevance = max(1, min(5, ai_relevance))
        title_zh = data.get("title_zh", "")
        highlights = data.get("highlights", "")
        return abstract_zh, tags, ai_relevance, title_zh, highlights
    except Exception as e:
        log.warning(f"Failed to parse Claude response: {e}\nRaw: {response[:200]}")
        return "翻译失败", [], 1, "", ""
