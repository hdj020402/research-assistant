"""Semantic Scholar API client supporting both authenticated and unauthenticated access."""
import os
import time
from typing import Optional
import requests
from shared.rate_limiter import RateLimiter

BASE_URL = "https://api.semanticscholar.org/graph/v1"

PAPER_FIELDS = (
    "paperId,title,abstract,year,citationCount,authors,externalIds,"
    "openAccessPdf,url,references,citations"
)
SEARCH_FIELDS = (
    "paperId,title,abstract,year,citationCount,authors,externalIds,"
    "openAccessPdf,url"
)

# Unauthenticated: ~100 req/5min ≈ 0.33/s; authenticated: 1/s
_unauth_limiter = RateLimiter(calls_per_second=0.3)
_auth_limiter = RateLimiter(calls_per_second=0.9)


class SemanticScholarClient:
    def __init__(self, use_api_key: bool = True):
        self.api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "") if use_api_key else ""
        self._limiter = _auth_limiter if self.api_key else _unauth_limiter

    @property
    def _headers(self) -> dict:
        h = {"Accept": "application/json"}
        if self.api_key:
            h["x-api-key"] = self.api_key
        return h

    def search_papers(self, query: str, limit: int = 20) -> list[dict]:
        """Search papers by keyword, sorted by citation count descending."""
        self._limiter.wait()
        url = f"{BASE_URL}/paper/search"
        params = {
            "query": query,
            "limit": limit,
            "fields": SEARCH_FIELDS,
            "sort": "citationCount:desc",
        }
        resp = requests.get(url, params=params, headers=self._headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])

    def get_paper(self, paper_id: str) -> Optional[dict]:
        """Fetch full paper details by Semantic Scholar paperId."""
        self._limiter.wait()
        url = f"{BASE_URL}/paper/{paper_id}"
        params = {"fields": PAPER_FIELDS}
        resp = requests.get(url, params=params, headers=self._headers, timeout=30)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()

    def get_references(self, paper_id: str, limit: int = 50) -> list[dict]:
        """Get papers that this paper references."""
        self._limiter.wait()
        url = f"{BASE_URL}/paper/{paper_id}/references"
        params = {"fields": SEARCH_FIELDS, "limit": limit}
        resp = requests.get(url, params=params, headers=self._headers, timeout=30)
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        data = resp.json()
        papers = []
        for ref in data.get("data", []):
            if ref.get("citedPaper"):
                papers.append(ref["citedPaper"])
        return papers

    def get_citations(self, paper_id: str, limit: int = 50) -> list[dict]:
        """Get papers that cite this paper."""
        self._limiter.wait()
        url = f"{BASE_URL}/paper/{paper_id}/citations"
        params = {"fields": SEARCH_FIELDS, "limit": limit}
        resp = requests.get(url, params=params, headers=self._headers, timeout=30)
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        data = resp.json()
        papers = []
        for cit in data.get("data", []):
            if cit.get("citingPaper"):
                papers.append(cit["citingPaper"])
        return papers

    def download_pdf(self, paper: dict, dest_path: str) -> bool:
        """
        Download open-access PDF if available. Returns True on success.
        """
        pdf_info = paper.get("openAccessPdf")
        if not pdf_info:
            return False
        pdf_url = pdf_info.get("url")
        if not pdf_url:
            return False
        try:
            self._limiter.wait()
            resp = requests.get(pdf_url, timeout=60, stream=True)
            resp.raise_for_status()
            import os
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except Exception:
            return False
