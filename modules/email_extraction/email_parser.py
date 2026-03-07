"""Parse journal ToC emails to extract article metadata."""
import re
from dataclasses import dataclass, field
from typing import Optional
from bs4 import BeautifulSoup


@dataclass
class ArticleItem:
    title: str
    authors: str = ""
    url: str = ""
    doi: str = ""
    abstract_from_email: str = ""
    journal: str = ""


# Publisher-specific selectors: {domain_fragment: (article_selector, title_sel, authors_sel, abstract_sel)}
PUBLISHER_SELECTORS = {
    "acs.org": {
        "article_block": "div.toc-item",
        "title": "a.toc-title",
        "authors": "span.toc-author",
        "abstract": "div.toc-abstract",
    },
    "rsc.org": {
        "article_block": "div.capsule",
        "title": "a.capsule__article-link",
        "authors": "div.capsule__authors",
        "abstract": "div.capsule__text",
    },
    "springer.com": {
        "article_block": "li.toc-item",
        "title": "h3.toc-item__title a",
        "authors": "span.toc-authors",
        "abstract": "div.toc-item__abstract",
    },
    "elsevier.com": {
        "article_block": "li.article-item",
        "title": "a.article-title",
        "authors": "span.article-authors",
        "abstract": "p.article-abstract",
    },
    "wiley.com": {
        "article_block": "div.issue-item",
        "title": "a.issue-item__title",
        "authors": "ul.rlist--inline",
        "abstract": "div.issue-item__abstract",
    },
}

# DOI pattern
DOI_PATTERN = re.compile(r"10\.\d{4,}/\S+")


def detect_journal(sender: str, subject: str) -> str:
    """Infer journal name from sender address and email subject."""
    sender_lower = sender.lower()
    subject_lower = subject.lower()

    if "acs.org" in sender_lower or "acs.pubs" in sender_lower:
        # Try to extract journal name from subject
        # e.g. "Journal of the American Chemical Society Table of Contents..."
        match = re.search(r"^(.+?)(?:\s+(?:table of contents|new articles|asap))", subject_lower)
        if match:
            return _title_case(match.group(1).strip())
        return "ACS"
    if "rsc.org" in sender_lower:
        return _extract_journal_from_subject(subject) or "RSC"
    if "springer.com" in sender_lower:
        return _extract_journal_from_subject(subject) or "Springer"
    if "elsevier.com" in sender_lower:
        return _extract_journal_from_subject(subject) or "Elsevier"
    if "wiley.com" in sender_lower:
        return _extract_journal_from_subject(subject) or "Wiley"
    return _extract_journal_from_subject(subject) or "Unknown"


def _title_case(s: str) -> str:
    return " ".join(w.capitalize() for w in s.split())


def _extract_journal_from_subject(subject: str) -> str:
    """Heuristically extract journal name from subject line."""
    # Strip common suffixes
    for pattern in [
        r"\s*[-–|:]\s*(?:table of contents|new articles|asap articles|just accepted).*$",
        r"\s+\d{4}-\d{2}-\d{2}.*$",
        r"\s+vol\.?\s*\d+.*$",
    ]:
        subject = re.sub(pattern, "", subject, flags=re.IGNORECASE)
    return subject.strip()[:60] if subject.strip() else ""


def parse_email(email_data: dict) -> list[ArticleItem]:
    """
    Parse a single email and return all ArticleItems found.

    Tries publisher-specific parsing first; falls back to generic DOI link extraction.
    """
    html_body = email_data.get("html_body", "")
    text_body = email_data.get("text_body", "")
    sender = email_data.get("sender", "")
    subject = email_data.get("subject", "")
    journal = detect_journal(sender, subject)

    articles: list[ArticleItem] = []

    if html_body:
        articles = _parse_html(html_body, sender, journal)

    # Fall back to plain-text DOI extraction if HTML parsing found nothing
    if not articles and text_body:
        articles = _parse_text_fallback(text_body, journal)

    # Deduplicate by DOI, preserving order
    seen_dois: set[str] = set()
    seen_urls: set[str] = set()
    unique: list[ArticleItem] = []
    for a in articles:
        key = a.doi or a.url
        if key and key not in seen_dois and key not in seen_urls:
            if a.doi:
                seen_dois.add(a.doi)
            if a.url:
                seen_urls.add(a.url)
            unique.append(a)
    return unique


def _parse_html(html: str, sender: str, journal: str) -> list[ArticleItem]:
    """Parse HTML email body for article entries."""
    soup = BeautifulSoup(html, "lxml")

    # Try publisher-specific selectors
    for domain, selectors in PUBLISHER_SELECTORS.items():
        if domain in sender.lower():
            articles = _extract_with_selectors(soup, selectors, journal)
            if articles:
                return articles

    # Generic extraction: find all DOI-bearing links
    return _generic_html_extraction(soup, journal)


def _extract_with_selectors(soup: BeautifulSoup, selectors: dict, journal: str) -> list[ArticleItem]:
    """Extract articles using publisher-specific CSS selectors."""
    articles = []
    blocks = soup.select(selectors["article_block"])
    for block in blocks:
        title_tag = block.select_one(selectors["title"])
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        if not title:
            continue

        url = title_tag.get("href", "")
        if url and not url.startswith("http"):
            url = "https://" + url.lstrip("/")

        doi = _extract_doi_from_url(url) or ""

        authors_tag = block.select_one(selectors.get("authors", ""))
        authors = authors_tag.get_text(strip=True) if authors_tag else ""

        abstract_tag = block.select_one(selectors.get("abstract", ""))
        abstract = abstract_tag.get_text(strip=True) if abstract_tag else ""

        articles.append(
            ArticleItem(
                title=title,
                authors=authors,
                url=url,
                doi=doi,
                abstract_from_email=abstract,
                journal=journal,
            )
        )
    return articles


def _generic_html_extraction(soup: BeautifulSoup, journal: str) -> list[ArticleItem]:
    """
    Generic extraction: walk all <a> tags, find DOI links, reconstruct article info
    from surrounding context.
    """
    articles = []
    processed_dois: set[str] = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        doi = _extract_doi_from_url(href)
        if not doi or doi in processed_dois:
            continue
        processed_dois.add(doi)

        title = a_tag.get_text(strip=True)
        if len(title) < 10:
            # Try parent elements for a meaningful title
            for parent in a_tag.parents:
                text = parent.get_text(strip=True)
                if len(text) > 10 and len(text) < 300:
                    title = text
                    break

        # Try to find abstract in nearby siblings
        abstract = ""
        parent = a_tag.parent
        if parent:
            for sibling in parent.next_siblings:
                sib_text = sibling.get_text(strip=True) if hasattr(sibling, "get_text") else ""
                if len(sib_text) > 50:
                    abstract = sib_text[:1000]
                    break

        url = href if href.startswith("http") else f"https://doi.org/{doi}"
        articles.append(
            ArticleItem(
                title=title[:200],
                url=url,
                doi=doi,
                abstract_from_email=abstract,
                journal=journal,
            )
        )
    return articles


def _parse_text_fallback(text: str, journal: str) -> list[ArticleItem]:
    """Extract DOIs from plain text email body as a last resort."""
    articles = []
    for match in DOI_PATTERN.finditer(text):
        doi = match.group().rstrip(".,;)")
        articles.append(
            ArticleItem(
                title=doi,
                doi=doi,
                url=f"https://doi.org/{doi}",
                journal=journal,
            )
        )
    return articles


def _extract_doi_from_url(url: str) -> Optional[str]:
    """Extract DOI from a URL string."""
    if not url:
        return None
    # Direct DOI link: https://doi.org/10.xxxx/...
    doi_match = DOI_PATTERN.search(url)
    if doi_match:
        return doi_match.group().rstrip(".,;)")
    return None
