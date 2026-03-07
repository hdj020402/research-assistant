"""Fetch full abstracts from publisher journal pages with graceful degradation."""
import requests
from bs4 import BeautifulSoup
from shared.rate_limiter import RateLimiter

# Per-publisher CSS selectors for abstract extraction
ABSTRACT_SELECTORS = {
    "pubs.acs.org": [
        "p.articleBody_abstractText",
        "div.articleBody_abstractText",
        "section.article_abstractText p",
    ],
    "www.nature.com": [
        "div#Abs1-content p",
        "section[data-title='Abstract'] p",
    ],
    "chemistry.rsc.org": [
        "div.abstract p",
        "p.abstract",
    ],
    "www.sciencedirect.com": [
        "div.abstract.author p",
        "div#abstracts p",
    ],
    "onlinelibrary.wiley.com": [
        "div.article-section__content p",
        "section.article-section__abstract p",
    ],
    "link.springer.com": [
        "div#Abs1-content p",
        "section.Abstract p",
    ],
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

_rate_limiter = RateLimiter(calls_per_second=0.5)  # max 1 request per 2 seconds


def fetch_abstract(url: str, timeout: int = 10) -> str:
    """
    Try to fetch the abstract from a journal article page.

    Returns empty string on any failure (graceful degradation).
    """
    if not url or not url.startswith("http"):
        return ""
    try:
        _rate_limiter.wait()
        response = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return _extract_abstract(response.text, response.url)
    except Exception:
        return ""


def _extract_abstract(html: str, final_url: str) -> str:
    """Extract abstract text using publisher-specific or generic selectors."""
    soup = BeautifulSoup(html, "lxml")

    # Try publisher-specific selectors
    for domain, selectors in ABSTRACT_SELECTORS.items():
        if domain in final_url:
            for selector in selectors:
                tag = soup.select_one(selector)
                if tag:
                    text = tag.get_text(separator=" ", strip=True)
                    if len(text) > 50:
                        return text

    # Generic fallback: look for common abstract patterns
    for selector in [
        "section[id*='abstract'] p",
        "div[class*='abstract'] p",
        "p[class*='abstract']",
        "div[id*='abstract'] p",
    ]:
        tags = soup.select(selector)
        for tag in tags:
            text = tag.get_text(separator=" ", strip=True)
            if len(text) > 50:
                return text

    return ""
