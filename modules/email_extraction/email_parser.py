"""Parse journal ToC emails to extract article metadata."""
import re
import logging
from dataclasses import dataclass
from typing import Optional
from bs4 import BeautifulSoup, Tag

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

# ── Section-based filtering ──────────────────────────────────────────────────
# Section names that contain research content (keep)
RESEARCH_SECTIONS = {
    "articles", "article", "letters", "letter",
    "reviews", "review", "mini reviews",
    "news & views", "news and views",
    "perspectives", "perspective",
    "communications", "communication", "rapid communications",
    "brief communications", "short communications",
    "research", "original research", "original articles",
    "reports", "report", "research reports",
    "accelerated articles", "asap articles", "just accepted",
    "full papers", "papers",
}

# Section names that contain non-research content (skip)
NON_RESEARCH_SECTIONS = {
    "editorial", "editorials", "from the editor",
    "world view", "world views",
    "news", "news in focus", "news in brief", "new online",
    "features", "feature",
    "multimedia", "video", "podcast", "podcasts",
    "book review", "book reviews", "books & arts", "books and arts",
    "comment", "comments", "commentary",
    "opinion", "opinions",
    "correspondence", "matters arising",
    "work", "careers", "career",
    "amendments & corrections", "amendments and corrections",
    "corrections", "correction", "errata", "erratum",
    "retraction", "retractions",
    "obituary", "obituaries",
    "this week", "the week ahead",
    "research highlights", "research highlight",
    "daily briefing",
    "technology feature", "toolbox",
}

ALL_KNOWN_SECTIONS = RESEARCH_SECTIONS | NON_RESEARCH_SECTIONS

# ── Title-based filtering (fallback) ─────────────────────────────────────────
NON_RESEARCH_TITLE_PATTERNS = [
    r"^editorial\b",
    r"^editor.?s?\s+(note|letter|choice|pick|highlight)",
    r"^world\s+view\b",
    r"^from\s+the\s+editor",
    r"^in\s+this\s+issue\b",
    r"^letter\s+to\s+the\s+editor",
    r"^(author|publisher|editor)\s+correction",
    r"^correction\s*(:|to)\s",
    r"^erratum\b",
    r"^retraction\b",
    r"^corrigendum\b",
    r"^editorial\s+expression\s+of\s+concern",
    r"^amendment\b",
    r"^advertisement\b",
    r"^sponsor(ed)?\b",
    r"^nature\s+briefing",
    # Section headers mistakenly captured as titles
    r"^(articles?|letters?|reviews?|research|opinion)\s*$",
]
_NON_RESEARCH_RE = [re.compile(p, re.IGNORECASE) for p in NON_RESEARCH_TITLE_PATTERNS]


def _is_non_research_title(title: str) -> bool:
    """Check if a title indicates non-research content."""
    for pattern in _NON_RESEARCH_RE:
        if pattern.search(title.strip()):
            return True
    return False


# ── Skip-link detection ──────────────────────────────────────────────────────
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

SKIP_LINK_DOMAINS = {
    "facebook.com", "twitter.com", "linkedin.com", "youtube.com",
    "instagram.com", "mailto:", "tel:", "#",
}


# ── Journal detection ────────────────────────────────────────────────────────
def detect_journal(sender: str, subject: str) -> str:
    """Infer journal name from sender address and email subject."""
    sender_lower = sender.lower()

    if "acs.org" in sender_lower or "acspubs.org" in sender_lower:
        match = re.search(
            r"(?:new articles for|latest articles from)\s+(.+?)(?:\s+are available|\s*$)",
            subject, re.IGNORECASE,
        )
        if match:
            return match.group(1).strip()
        match = re.search(r"^(.+?)(?:\s+(?:table of contents|new articles|asap|most-read))", subject, re.IGNORECASE)
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


# ── Main entry point ─────────────────────────────────────────────────────────
def parse_email(email_data: dict) -> list[ArticleItem]:
    """
    Parse a single email and return all ArticleItems found.

    Strategy:
    1. Try DOI-based extraction (works for ACS direct links)
    2. Try section-aware link-text extraction (works for Nature/Springer tracking URLs)
    3. Fall back to plain-text DOI extraction
    Then filter non-research content by title patterns.
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

        # Strategy 2: Section-aware link-text extraction (for tracking URLs)
        if not articles:
            articles = _extract_by_link_text(soup, journal)

    # Fall back to plain-text DOI extraction
    if not articles and text_body:
        articles = _parse_text_fallback(text_body, journal)

    # Title-based filtering (catches remaining non-research items)
    before_filter = len(articles)
    articles = [a for a in articles if not _is_non_research_title(a.title)]
    filtered_count = before_filter - len(articles)
    if filtered_count:
        log.info(f"  Filtered {filtered_count} non-research items by title")

    # Deduplicate
    unique = _deduplicate(articles)
    return unique


# ── Extraction strategies ────────────────────────────────────────────────────
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
    Section-aware extraction: walk HTML in document order, track section headers,
    and only extract links from research sections.
    """
    articles = []
    seen_urls: set[str] = set()

    # Track current section state
    in_research_section = True  # default: keep (for emails without section headers)
    found_any_section = False

    for element in soup.descendants:
        if not isinstance(element, Tag):
            continue

        # ── Check if this element is a section header ──
        # Section headers: not a link, not inside a link, short text matching known sections
        if element.name != "a" and not element.find_parent("a"):
            text = element.get_text(strip=True)
            text_lower = text.lower().strip()
            if text_lower and len(text_lower) < 40 and text_lower in ALL_KNOWN_SECTIONS:
                found_any_section = True
                in_research_section = text_lower in RESEARCH_SECTIONS
                continue

        # ── Process links ──
        if element.name != "a" or not element.get("href"):
            continue

        # Skip if we're in a non-research section
        if found_any_section and not in_research_section:
            continue

        href = element["href"]
        if not href or not href.startswith("http"):
            continue
        if href in seen_urls:
            continue

        # Skip navigation/social/utility links
        if _is_skip_link(element, href):
            continue

        title = element.get_text(strip=True)
        if not title:
            continue

        # Article titles: 20-300 chars
        if len(title) < 20 or len(title) > 300:
            continue

        # Skip navigation-looking text
        if _looks_like_navigation(title):
            continue

        seen_urls.add(href)

        abstract = _find_nearby_text(element, min_len=30)
        authors = _find_nearby_authors(element)
        doi = _extract_doi_from_url(href) or _find_nearby_doi(element) or ""

        articles.append(ArticleItem(
            title=title,
            url=href,
            doi=doi,
            abstract_from_email=abstract,
            authors=authors,
            journal=journal,
        ))

    if found_any_section:
        kept = len(articles)
        log.info(f"  Section-aware filtering applied: kept {kept} research articles")

    return articles


# ── Helper functions ─────────────────────────────────────────────────────────
def _is_skip_link(a_tag: Tag, href: str) -> bool:
    """Check if a link should be skipped (navigation, social, etc.)."""
    href_lower = href.lower()
    for domain in SKIP_LINK_DOMAINS:
        if domain in href_lower:
            return True
    text = a_tag.get_text(strip=True).lower()
    if not text:
        return True
    for skip_text in SKIP_LINK_TEXTS:
        if text == skip_text or (len(text) < 30 and skip_text in text):
            return True
    if a_tag.find("img") and len(text) < 5:
        return True
    return False


def _looks_like_navigation(text: str) -> bool:
    """Check if text looks like a navigation element rather than an article title."""
    if len(text) < 15:
        return True
    if text.isupper() and len(text) < 40:
        return True
    if not any(c.isalpha() for c in text):
        return True
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
    parent = a_tag.parent
    if not parent:
        return ""
    for sibling in a_tag.next_siblings:
        if hasattr(sibling, "get_text"):
            text = sibling.get_text(strip=True)
            if len(text) >= min_len:
                return text[:1000]
    for sibling in parent.next_siblings:
        if hasattr(sibling, "get_text"):
            text = sibling.get_text(strip=True)
            if len(text) >= min_len:
                return text[:1000]
    for ancestor in a_tag.parents:
        if ancestor.name in ("td", "div"):
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
    for ancestor in a_tag.parents:
        if ancestor.name in ("td", "div", "tr"):
            bold_tags = ancestor.find_all(["b", "strong"])
            for bold in bold_tags:
                text = bold.get_text(strip=True)
                if text and ("," in text or "et al" in text.lower() or "&" in text):
                    if 5 < len(text) < 500:
                        return text
            break
    return ""


def _find_nearby_doi(a_tag: Tag) -> str:
    """Try to find a DOI in the text near a link element."""
    for ancestor in a_tag.parents:
        if ancestor.name in ("td", "div", "tr", "li"):
            text = ancestor.get_text(separator=" ", strip=True)
            match = DOI_PATTERN.search(text)
            if match:
                return match.group().rstrip(".,;)")
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
                title=doi, doi=doi,
                url=f"https://doi.org/{doi}", journal=journal,
            ))
    return articles


def _deduplicate(articles: list[ArticleItem]) -> list[ArticleItem]:
    """Deduplicate articles by URL and title."""
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    unique: list[ArticleItem] = []
    for a in articles:
        if a.url and a.url in seen_urls:
            continue
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
