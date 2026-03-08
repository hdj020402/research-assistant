"""Fetch paper metadata (abstract, DOI) from Semantic Scholar API."""
import os
import logging
import requests
from shared.rate_limiter import RateLimiter

log = logging.getLogger(__name__)

S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "abstract,externalIds,title,tldr"

_api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
_rate_limiter = RateLimiter(calls_per_second=0.9 if _api_key else 0.3)


def fetch_paper_metadata(doi: str = "", title: str = "", timeout: int = 10) -> dict:
    """
    Query Semantic Scholar for paper abstract and DOI.

    Tries DOI lookup first, then title search as fallback.
    Returns dict with keys: 'abstract', 'doi', 'tldr' (empty strings if not found).
    """
    headers = {"Accept": "application/json"}
    if _api_key:
        headers["x-api-key"] = _api_key

    # Try DOI lookup first (fast, exact match)
    if doi:
        result = _lookup_by_doi(doi, headers, timeout)
        if result["abstract"]:
            return result

    # Fall back to title search
    if title:
        result = _search_by_title(title, headers, timeout)
        if result["abstract"] or result["doi"]:
            # Preserve original DOI if we already have it
            if doi and not result["doi"]:
                result["doi"] = doi
            return result

    return {"abstract": "", "doi": doi, "tldr": ""}
def _lookup_by_doi(doi: str, headers: dict, timeout: int) -> dict:
    try:
        _rate_limiter.wait()
        resp = requests.get(
            f"{S2_BASE}/paper/DOI:{doi}",
            params={"fields": S2_FIELDS},
            headers=headers,
            timeout=timeout,
        )
        if resp.status_code == 200:
            return _extract(resp.json())
        log.debug(f"S2 DOI lookup returned {resp.status_code} for {doi}")
    except Exception as e:
        log.debug(f"S2 DOI lookup failed for {doi}: {e}")
    return {"abstract": "", "doi": doi, "tldr": ""}
def _search_by_title(title: str, headers: dict, timeout: int) -> dict:
    try:
        _rate_limiter.wait()
        resp = requests.get(
            f"{S2_BASE}/paper/search",
            params={"query": title[:200], "fields": S2_FIELDS, "limit": 1},
            headers=headers,
            timeout=timeout,
        )
        if resp.status_code == 200:
            papers = resp.json().get("data", [])
            if papers:
                return _extract(papers[0])
    except Exception as e:
        log.debug(f"S2 title search failed for '{title[:50]}': {e}")
    return {"abstract": "", "doi": "", "tldr": ""}


def _extract(paper: dict) -> dict:
    abstract = paper.get("abstract", "") or ""
    external_ids = paper.get("externalIds", {}) or {}
    doi = external_ids.get("DOI", "") or ""
    tldr_data = paper.get("tldr")
    tldr = tldr_data.get("text", "") if isinstance(tldr_data, dict) else ""
    return {"abstract": abstract, "doi": doi, "tldr": tldr}
