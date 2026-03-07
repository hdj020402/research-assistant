"""Parse journal ToC emails to extract article metadata."""
import re
import logging
from dataclasses import dataclass
from typing import Optional
from bs4 import BeautifulSoup, Tag
import requests

log = logging.getLogger(__name__)


@dataclass
class ArticleItem:
    title: str
    authors: str = ""
    url: str = ""
    doi: str = ""
    abstract_from_email: str = ""
    journal: str = ""


# DOI pattern
DOI_PATTERN = re.compile(r"10\.\d{4,}/\S+")

# Known publisher article URL patterns (after redirect resolution)
PUBLISHER_ARTICLE_PATTERNS = [
    re.compile(r"nature\.com/articles/"),
    re.compile(r"pubs\.acs\.org/doi/"),
    re.compile(r"doi\.org/10\."),
    re.compile(r"link\.springer\.com/article/"),
    re.compile(r"sciencedirect\.com/science/article/"),
    re.compile(r"onlinelibrary\.wiley\.com/doi/"),
    re.compile(r"pubs\.rsc\.org/en/content/"),
    re.compile(r"cell\.com/.+/fulltext"),
    re.compile(r"science\.org/doi/"),
    re.compile(r"acs\.org/doi/"),
]

# Known tracking URL domains (these redirect to real article URLs)
TRACKING_DOMAINS = [
    "links.springernature.com",
    "click.e.nature.com",
    "click.acs.org",
    "click.email.rsc.org",
    "links.email.wiley.com",
    "t.email.elsevier.com",
]

# Titles matching these patterns are non-research content → skip
NON_RESEARCH_TITLE_PATTERNS = [
    # Editorials, opinions, commentary
    r"^editorial\b",
    r"^editor.?s?\s+(note|letter|choice|pick|highlight)",
    r"^world\s+view\b",
    r"^comment(ary)?\s*:",
    r"^from\s+the\s+editor",
    r"^in\s+this\s+issue\b",
    r"^letter\s+to\s+the\s+editor",
    # News, media, non-research
    r"^news\s*(:|in\s+focus|in\s+brief|feature|\&)",
    r"^research\s+highlight",
    r"^daily\s+briefing",
    r"^book\s+review",
    r"^obituary\b",
    r"^podcast\b",
    r"^video\b",
    r"^multimedia\b",
    r"^infographic\b",
    r"^events?\s*:",
    r"^Q\s*&\s*A\s*:",
    # Corrections, errata
    r"^(author|publisher|editor)\s+correction",
    r"^correction\s*(:|to)\s",
    r"^erratum\b",
    r"^retraction\b",
    r"^corrigendum\b",
    r"^editorial\s+expression\s+of\s+concern",
    r"^amendment\b",
    # Correspondence (not research)
    r"^correspondence\s*:",
    r"^reply\s+to\s*:",
    r"^response\s+to\s*:",
    # Advertisements, career, misc
    r"^advertisement\b",
    r"^sponsor(ed)?\b",
    r"^career\b",
    r"^job\b",
    r"^nature\s+briefing",
    r"^this\s+week\b",
    r"^the\s+week\s+ahead",
    # Section headers mistakenly captured as titles
    r"^(articles?|letters?|reviews?|research|opinion)\s*$",
]
_NON_RESEARCH_RE = [re.compile(p, re.IGNORECASE) for p in NON_RESEARCH_TITLE_PATTERNS]


def _is_non_research(title: str) -> bool:
    """Check if a title indicates non-research content."""
    title_stripped = title.strip()
    for pattern in _NON_RESEARCH_RE:
        if pattern.search(title_stripped):
            return True
    return False
SKIP_LINK_TEXTS = {
    "unsubscribe", "manage preferences", "privacy policy", "view in browser",
    "view online", "contact us", "terms of use", "cookie policy",
    "forward to a friend", "update profile", "sign in", "log in",
    "facebook", "twitter", "linkedin", "youtube", "instagram",
    "read more", "more news", "see all", "view all", "browse",
    "about us", "advertise", "careers", "help", "feedback",
    "subscribe", "renew", "register", "download the app",
    "nature.com", "acs.org", "rsc.org", "wiley.com", "springer.com",
}

# Domains that are definitely not article links
SKIP_LINK_DOMAINS = {
    "facebook.com", "twitter.com", "linkedin.com", "youtube.com",
    "instagram.com", "mailto:", "tel:", "#",
}


def detect_journal(sender: str, subject: str) -> str:
    """Infer journal name from sender address and email subject."""
    sender_lower = sender.lower()
    subject_lower = subject.lower()

    if "acs.org" in sender_lower or "acspubs.org" in sender_lower:
        # e.g. "These new articles for Journal of Chemical Information and Modeling are available online."
        match = re.search(
            r"(?:new articles for|latest articles from)\s+(.+?)(?:\s+are available|\s*$)",
            subject, re.IGNORECASE,
        )
        if match:
            return match.group(1).strip()
        match = re.search(r"^(.+?)(?:\s+(?:table of contents|new articles|asap|most-read))", subject_lower)
        if match:
            return _title_case(match.group(1).strip())
        return "ACS"
    if "nature.com" in sender_lower:
        match = re.search(r"^(.+?)\s+alert\b", subject, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return _extract_journal_from_subject(subject) or "Nature"
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
    for pattern in [
        r"\s*[-–|:]\s*(?:table of contents|new articles|asap articles|just accepted).*$",
        r"\s+\d{4}-\d{2}-\d{2}.*$",
        r"\s+vol\.?\s*\d+.*$",
        r"\s+alert\s+for\s+.*$",
    ]:
        subject = re.sub(pattern, "", subject, flags=re.IGNORECASE)
    return subject.strip()[:60] if subject.strip() else ""


def parse_email(email_data: dict) -> list[ArticleItem]:
    """
    Parse a single email and return all ArticleItems found.

    Strategy:
    1. Try DOI-based extraction (works for ACS direct links)
    2. Try link-text-based extraction (works for Nature/Springer tracking URLs)
    3. Fall back to plain-text DOI extraction
    """
    html_body = email_data.get("html_body", "")
    text_body = email_data.get("text_body", "")
    sender = email_data.get("sender", "")
    subject = email_data.get("subject", "")
    journal = detect_journal(sender, subject)

    articles: list[ArticleItem] = []

    if html_body:
        soup = BeautifulSoup(html_body, "lxml")

        # Strategy 1: Extract articles with DOIs in URLs
        doi_articles = _extract_doi_links(soup, journal)
        if doi_articles:
            articles = doi_articles

        # Strategy 2: Extract articles by link text (for tracking URLs)
        if not articles:
            articles = _extract_by_link_text(soup, journal)

    # Fall back to plain-text DOI extraction
    if not articles and text_body:
        articles = _parse_text_fallback(text_body, journal)

    # Filter out non-research content (editorials, news, corrections, etc.)
    before_filter = len(articles)
    articles = [a for a in articles if not _is_non_research(a.title)]
    filtered_count = before_filter - len(articles)
    if filtered_count:
        log.info(f"  Filtered {filtered_count} non-research items (editorials, news, corrections, etc.)")

    # Deduplicate by URL (primary) and title (secondary)
    unique = _deduplicate(articles)
    log.debug(f"  Parsed {len(unique)} unique articles from '{subject}'")
    return unique


def _extract_doi_links(soup: BeautifulSoup, journal: str) -> list[ArticleItem]:
    """Extract articles where the URL contains a DOI."""
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
            title = _find_nearby_title(a_tag)

        abstract = _find_nearby_text(a_tag, min_len=50)
        url = href if href.startswith("http") else f"https://doi.org/{doi}"

        articles.append(ArticleItem(
            title=title[:300] if title else doi,
            url=url,
            doi=doi,
            abstract_from_email=abstract,
            journal=journal,
        ))
    return articles


def _extract_by_link_text(soup: BeautifulSoup, journal: str) -> list[ArticleItem]:
    """
    Extract articles by identifying links with substantial text that look like article titles.
    Works for emails with tracking URLs (Nature, Springer, etc.)
    """
    articles = []
    seen_urls: set[str] = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if not href or not href.startswith("http"):
            continue
        if href in seen_urls:
            continue

        # Skip non-article links
        if _is_skip_link(a_tag, href):
            continue

        title = a_tag.get_text(strip=True)
        if not title:
            continue

        # Article titles are typically 20-300 chars
        if len(title) < 20 or len(title) > 300:
            continue

        # Skip if title looks like a navigation element (all caps short text, etc.)
        if _looks_like_navigation(title):
            continue

        seen_urls.add(href)

        # Try to find abstract/description near this link
        abstract = _find_nearby_text(a_tag, min_len=30)

        # Try to find authors near this link
        authors = _find_nearby_authors(a_tag)

        # Try to extract DOI from URL
        doi = _extract_doi_from_url(href) or ""

        articles.append(ArticleItem(
            title=title,
            url=href,
            doi=doi,
            abstract_from_email=abstract,
            authors=authors,
            journal=journal,
        ))

    return articles


def _is_skip_link(a_tag: Tag, href: str) -> bool:
    """Check if a link should be skipped (navigation, social, etc.)."""
    href_lower = href.lower()

    # Skip known non-article domains
    for domain in SKIP_LINK_DOMAINS:
        if domain in href_lower:
            return True

    # Get link text
    text = a_tag.get_text(strip=True).lower()
    if not text:
        return True

    # Skip known non-article text patterns
    for skip_text in SKIP_LINK_TEXTS:
        if text == skip_text or (len(text) < 30 and skip_text in text):
            return True

    # Skip if the link contains only an image (no text)
    if a_tag.find("img") and len(text) < 5:
        return True

    return False


def _looks_like_navigation(text: str) -> bool:
    """Check if text looks like a navigation element rather than an article title."""
    # Very short text
    if len(text) < 15:
        return True
    # All uppercase short text (section headers)
    if text.isupper() and len(text) < 40:
        return True
    # Only numbers/special chars
    if not any(c.isalpha() for c in text):
        return True
    # Common navigation patterns
    nav_patterns = [
        r"^vol(ume)?\.?\s*\d+",
        r"^issue\s*\d+",
        r"^\d+\s*(january|february|march|april|may|june|july|august|september|october|november|december)",
        r"^page\s*\d+",
    ]
    text_lower = text.lower()
    for pat in nav_patterns:
        if re.match(pat, text_lower):
            return True
    return False


def _find_nearby_title(a_tag: Tag) -> str:
    """Try to find a meaningful title text near the link."""
    for parent in a_tag.parents:
        if parent.name in ("td", "div", "li", "tr"):
            text = parent.get_text(strip=True)
            if 10 < len(text) < 300:
                return text
    return a_tag.get_text(strip=True)


def _find_nearby_text(a_tag: Tag, min_len: int = 50) -> str:
    """Try to find descriptive text (abstract) near a link element."""
    # Look in parent container for text blocks
    parent = a_tag.parent
    if not parent:
        return ""

    # Check siblings after the link
    for sibling in a_tag.next_siblings:
        if hasattr(sibling, "get_text"):
            text = sibling.get_text(strip=True)
            if len(text) >= min_len:
                return text[:1000]

    # Check parent's siblings
    for sibling in parent.next_siblings:
        if hasattr(sibling, "get_text"):
            text = sibling.get_text(strip=True)
            if len(text) >= min_len:
                return text[:1000]

    # Walk up and check nearby table cells
    for ancestor in a_tag.parents:
        if ancestor.name in ("td", "div"):
            # Get text from this cell excluding the link itself
            texts = []
            for child in ancestor.children:
                if child != a_tag and hasattr(child, "get_text"):
                    t = child.get_text(strip=True)
                    if t and t != a_tag.get_text(strip=True):
                        texts.append(t)
            combined = " ".join(texts)
            if len(combined) >= min_len:
                return combined[:1000]
            break

    return ""


def _find_nearby_authors(a_tag: Tag) -> str:
    """Try to find author names near a link element."""
    # Authors are typically in bold text after title/abstract
    for ancestor in a_tag.parents:
        if ancestor.name in ("td", "div", "tr"):
            bold_tags = ancestor.find_all(["b", "strong"])
            for bold in bold_tags:
                text = bold.get_text(strip=True)
                # Authors typically contain commas, "et al.", or "&"
                if text and ("," in text or "et al" in text.lower() or "&" in text):
                    if 5 < len(text) < 500:
                        return text
            break
    return ""


def _parse_text_fallback(text: str, journal: str) -> list[ArticleItem]:
    """Extract DOIs from plain text email body as a last resort."""
    articles = []
    seen = set()
    for match in DOI_PATTERN.finditer(text):
        doi = match.group().rstrip(".,;)")
        if doi not in seen:
            seen.add(doi)
            articles.append(ArticleItem(
                title=doi,
                doi=doi,
                url=f"https://doi.org/{doi}",
                journal=journal,
            ))
    return articles


def _deduplicate(articles: list[ArticleItem]) -> list[ArticleItem]:
    """Deduplicate articles by URL and title."""
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    unique: list[ArticleItem] = []

    for a in articles:
        # Primary dedup by URL
        if a.url and a.url in seen_urls:
            continue
        # Secondary dedup by normalized title
        title_key = re.sub(r"\s+", " ", a.title.lower().strip())
        if title_key in seen_titles:
            continue

        if a.url:
            seen_urls.add(a.url)
        seen_titles.add(title_key)
        unique.append(a)

    return unique


def _extract_doi_from_url(url: str) -> Optional[str]:
    """Extract DOI from a URL string."""
    if not url:
        return None
    doi_match = DOI_PATTERN.search(url)
    if doi_match:
        return doi_match.group().rstrip(".,;)")
    return None
