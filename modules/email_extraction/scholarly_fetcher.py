"""Fetch paper metadata (abstract, DOI) from Semantic Scholar API."""
import os
import logging
import time
import requests
from shared.rate_limiter import RateLimiter

log = logging.getLogger(__name__)

S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "abstract,externalIds,title,tldr"

_api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
_rate_limiter = RateLimiter(calls_per_second=0.5)  # shared across all S2 endpoints


def fetch_paper_metadata(doi: str = "", title: str = "", timeout: int = 5) -> dict:
    """
    Query Semantic Scholar for paper abstract and DOI.

    Tries DOI lookup first, then title match as fallback.
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

    # Fall back to title match (single best match, 404 if not found)
    if title:
        result = _match_by_title(title, headers, timeout)
        if result["abstract"] or result["doi"]:
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
        log.info(f"S2 DOI lookup returned {resp.status_code} for {doi}")
    except Exception as e:
        log.info(f"S2 DOI lookup failed for {doi}: {e}")
    return {"abstract": "", "doi": doi, "tldr": ""}


def _match_by_title(title: str, headers: dict, timeout: int) -> dict:
    """Use /paper/search/match for exact title matching (returns single best match or 404)."""
    for attempt in range(2):
        try:
            _rate_limiter.wait()
            resp = requests.get(
                f"{S2_BASE}/paper/search/match",
                params={"query": title[:300], "fields": S2_FIELDS},
                headers=headers,
                timeout=timeout,
            )
            if resp.status_code == 200:
                data = resp.json().get("data", [])
                if data:
                    return _extract(data[0])
                return {"abstract": "", "doi": "", "tldr": ""}
            elif resp.status_code == 404:
                # No matching paper found — expected for new papers
                log.info(f"S2 title match: not found for '{title[:60]}'")
                return {"abstract": "", "doi": "", "tldr": ""}
            elif resp.status_code == 429:
                if attempt == 0:
                    log.info("S2 rate limited (429), retrying in 3s...")
                    time.sleep(3)
                    continue
                log.warning("S2 rate limited (429) after retry, skipping")
            else:
                log.info(f"S2 title match returned {resp.status_code}")
            return {"abstract": "", "doi": "", "tldr": ""}
        except Exception as e:
            log.info(f"S2 title match failed for '{title[:60]}': {e}")
            return {"abstract": "", "doi": "", "tldr": ""}
    return {"abstract": "", "doi": "", "tldr": ""}


def _extract(paper: dict) -> dict:
    abstract = paper.get("abstract", "") or ""
    external_ids = paper.get("externalIds", {}) or {}
    doi = external_ids.get("DOI", "") or ""
    tldr_data = paper.get("tldr")
    tldr = tldr_data.get("text", "") if isinstance(tldr_data, dict) else ""
    return {"abstract": abstract, "doi": doi, "tldr": tldr}
