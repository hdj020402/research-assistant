"""Fetch full abstracts from publisher journal pages with graceful degradation."""
import logging
from curl_cffi import requests
from bs4 import BeautifulSoup
from shared.rate_limiter import RateLimiter

log = logging.getLogger(__name__)

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

_rate_limiter = RateLimiter(calls_per_second=0.5)  # max 1 request per 2 seconds


def fetch_abstract(url: str, timeout: int = 10) -> str:
    """
    Try to fetch the abstract from a journal article page.

    Uses curl_cffi with Chrome impersonation to bypass Cloudflare.
    Returns empty string on any failure (graceful degradation).
    """
    if not url or not url.startswith("http"):
        return ""
    try:
        _rate_limiter.wait()
        response = requests.get(
            url, impersonate="chrome", timeout=timeout, allow_redirects=True,
        )
        response.raise_for_status()
        return _extract_abstract(response.text, str(response.url))
    except Exception:
        return ""


def fetch_abstract_by_doi(doi: str, timeout: int = 10) -> str:
    """
    Fetch abstract using DOI → doi.org redirect → publisher page.

    This bypasses email tracking URLs and goes directly to the article.
    Returns empty string on any failure.
    """
    if not doi:
        return ""
    url = f"https://doi.org/{doi}"
    log.debug(f"Fetching abstract via DOI: {url}")
    return fetch_abstract(url, timeout=timeout)


def _extract_abstract(html: str, final_url: str) -> str:
    """Extract abstract text using publisher-specific or generic selectors."""
    soup = BeautifulSoup(html, "lxml")

    # Remove reference superscripts (e.g. Nature uses <sup> for citation numbers)
    for sup in soup.find_all("sup"):
        sup.decompose()

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
