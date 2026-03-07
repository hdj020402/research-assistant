"""Deep analysis of individual papers using Claude Opus."""
import json
import re
from dataclasses import dataclass
from shared.claude_client import ClaudeClient
from shared.rate_limiter import RateLimiter
from modules.domain_deepdive.citation_graph import PaperNode

_rate_limiter = RateLimiter(calls_per_second=0.3)

SYSTEM_PROMPT = (
    "You are an expert scientific researcher specializing in AI for Chemistry. "
    "Analyze academic papers deeply and return structured JSON. "
    "Always respond with valid JSON only, no markdown code blocks or extra text."
)


@dataclass
class PaperAnalysis:
    problem: str
    methodology: str
    key_results: str
    open_questions: str
    significance: str


def analyze_paper(node: PaperNode, claude: ClaudeClient) -> PaperAnalysis:
    """
    Use Claude Opus to produce a deep analysis of a paper.
    Falls back to simple extraction if abstract is absent.
    """
    _rate_limiter.wait()

    abstract_text = node.abstract if node.abstract else "Abstract not available."
    prompt = f"""Analyze this research paper and return a JSON object with these exact keys:
- "problem": What scientific problem or gap does this paper address? (2-4 sentences)
- "methodology": What methods, models, or approaches are proposed/used? (2-4 sentences)
- "key_results": What are the main findings and quantitative results? (2-4 sentences)
- "open_questions": What problems remain unsolved or are identified as future work? (1-3 sentences)
- "significance": Why is this paper important to its field? What was its impact? (2-3 sentences)

Paper: "{node.title}" ({node.year})
Authors: {", ".join(node.authors[:5])}
Citation count: {node.citation_count}
Abstract: {abstract_text}

Respond with JSON only."""

    result = claude.opus(prompt, system=SYSTEM_PROMPT)
    return _parse_analysis(result)


def _parse_analysis(response: str) -> PaperAnalysis:
    """Parse Claude's JSON response into PaperAnalysis."""
    try:
        cleaned = re.sub(r"```(?:json)?\s*|\s*```", "", response.strip())
        data = json.loads(cleaned)
        return PaperAnalysis(
            problem=data.get("problem", "Analysis unavailable."),
            methodology=data.get("methodology", "Analysis unavailable."),
            key_results=data.get("key_results", "Analysis unavailable."),
            open_questions=data.get("open_questions", "Analysis unavailable."),
            significance=data.get("significance", "Analysis unavailable."),
        )
    except Exception:
        return PaperAnalysis(
            problem="Analysis failed.",
            methodology="Analysis failed.",
            key_results="Analysis failed.",
            open_questions="Analysis failed.",
            significance="Analysis failed.",
        )
