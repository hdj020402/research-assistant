"""Entry point for Module 1: Email Journal Abstract Extraction."""
import re
import sys
import logging
from datetime import datetime
import pytz

from shared.config_loader import load_config
from shared.claude_client import ClaudeClient
from modules.email_extraction.gmail_client import fetch_toc_emails, send_summary_email
from modules.email_extraction.email_parser import parse_email
from modules.email_extraction.abstract_fetcher import fetch_abstract
from modules.email_extraction.scholarly_fetcher import fetch_paper_metadata
from modules.email_extraction.translator import translate
from modules.email_extraction.claude_processor import process_article
from modules.email_extraction.report_generator import (
    write_article_note,
    write_weekly_index,
    generate_html_email,
    _week_range,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def _keyword_filter(articles, keywords):
    """
    Pre-filter articles by relevance keywords (case-insensitive).
    Matches against title and abstract_from_email.
    Returns (matched, skipped_count).
    """
    if not keywords:
        return articles, 0

    # Compile patterns once (word boundary aware where possible)
    patterns = [re.compile(re.escape(kw), re.IGNORECASE) for kw in keywords]

    matched = []
    for article in articles:
        text = f"{article.title} {article.abstract_from_email}"
        if any(p.search(text) for p in patterns):
            matched.append(article)

    return matched, len(articles) - len(matched)


def main():
    config = load_config("config.yml")
    claude = ClaudeClient(config)

    tz = config["global"]["timezone"]
    now = datetime.now(pytz.timezone(tz))
    date_added = now.strftime("%Y-%m-%d")
    week = _week_range(tz)

    email_cfg = config["email_extraction"]
    proc_cfg = email_cfg["processing"]
    out_cfg = email_cfg["output"]

    log.info(f"Starting email extraction for week {week}")

    # Step 1: Fetch ToC emails
    log.info("Fetching ToC emails from Gmail...")
    emails = fetch_toc_emails(
        sender_patterns=email_cfg["sender_patterns"],
        subject_patterns=email_cfg["subject_patterns"],
        lookback_days=proc_cfg["lookback_days"],
        timezone=tz,
    )
    log.info(f"Found {len(emails)} matching emails")

    if not emails:
        log.warning("No matching emails found. Exiting.")
        sys.exit(0)

    # Step 2: Parse all emails → ArticleItems
    all_articles_raw = []
    for email_data in emails:
        items = parse_email(email_data)
        log.info(
            f"  Email '{email_data['subject']}': found {len(items)} articles"
        )
        all_articles_raw.extend(items)

    log.info(f"Total articles parsed: {len(all_articles_raw)}")

    if not all_articles_raw:
        log.warning("No articles found in emails. Exiting.")
        sys.exit(0)

    # Step 3: Keyword pre-filter (before Claude to save tokens)
    keywords = proc_cfg.get("relevance_keywords", [])
    if keywords:
        all_articles_raw, skipped = _keyword_filter(all_articles_raw, keywords)
        log.info(
            f"Keyword pre-filter: {len(all_articles_raw)} matched, "
            f"{skipped} skipped ({len(keywords)} keywords)"
        )
        if not all_articles_raw:
            log.warning("No articles matched relevance keywords. Exiting.")
            sys.exit(0)

    # Step 4: Fetch abstracts and DOIs (Semantic Scholar → web scrape → email fallback)
    s2_tldrs = {}  # title → TLDR text from S2
    if proc_cfg.get("fetch_web_abstract", True):
        timeout = proc_cfg.get("web_fetch_timeout_seconds", 10)
        s2_count, web_count = 0, 0
        for i, article in enumerate(all_articles_raw):
            label = f"[{i+1}/{len(all_articles_raw)}]"

            # Try Semantic Scholar first (returns abstract + DOI + TLDR)
            s2 = fetch_paper_metadata(
                doi=article.doi, title=article.title, timeout=timeout,
            )

            if s2["tldr"]:
                s2_tldrs[article.title] = s2["tldr"]

            if s2["abstract"]:
                article.abstract_from_email = s2["abstract"]
                s2_count += 1
                log.info(f"  {label} S2 abstract: {article.title[:50]}")
            elif article.url:
                # Fall back to web scraping
                fetched = fetch_abstract(article.url, timeout=timeout)
                if fetched:
                    article.abstract_from_email = fetched
                    web_count += 1
                    log.info(f"  {label} Web abstract: {article.title[:50]}")
                elif not article.abstract_from_email:
                    log.warning(f"  {label} No abstract: {article.title[:50]}")

            # Fill in DOI if missing
            if not article.doi and s2["doi"]:
                article.doi = s2["doi"]

        log.info(
            f"Abstracts: {s2_count} from S2, {web_count} from web, "
            f"{len(all_articles_raw) - s2_count - web_count} from email/none"
        )

    # After fetching abstracts, re-run keyword filter for articles that now have abstracts
    if keywords:
        all_articles_raw, skipped2 = _keyword_filter(all_articles_raw, keywords)
        if skipped2:
            log.info(f"Post-abstract keyword filter: {skipped2} more skipped")

    # Step 5: Translate + Claude analysis
    processed = []
    log.info(f"Processing {len(all_articles_raw)} articles...")
    for i, article in enumerate(all_articles_raw):
        label = f"[{i+1}/{len(all_articles_raw)}]"
        log.info(f"  {label} {article.title[:60]}")

        # Translate title and abstract (DeepL → Google → Baidu fallback)
        title_zh = translate(article.title)
        abstract_zh = ""
        if article.abstract_from_email:
            abstract_zh = translate(article.abstract_from_email)

        if title_zh and abstract_zh:
            log.info(f"    Translated (API)")
        elif title_zh or abstract_zh:
            log.info(f"    Partially translated (API), Haiku will complete")
        else:
            log.info(f"    Translation API unavailable, Haiku will translate")

        try:
            result = process_article(
                title=article.title,
                abstract=article.abstract_from_email,
                journal=article.journal,
                doi=article.doi,
                url=article.url,
                authors=article.authors,
                pub_date="",
                claude=claude,
                tldr=s2_tldrs.get(article.title, ""),
                title_zh=title_zh,
                abstract_zh=abstract_zh,
            )
            processed.append(result)
        except Exception as e:
            log.error(f"    Failed to process article: {e}")

    log.info(f"Successfully processed {len(processed)} articles")

    # Step 6: Write Obsidian notes
    notes_dir = out_cfg["notes_dir"]
    log.info(f"Writing Obsidian notes to {notes_dir}/{week}/")
    for article in processed:
        try:
            path = write_article_note(article, notes_dir, week, date_added)
            log.info(f"  Written: {path.name}")
        except Exception as e:
            log.error(f"  Failed to write note for '{article.title[:40]}': {e}")

    # Step 7: Write weekly index
    index_path = write_weekly_index(notes_dir, week, len(processed))
    log.info(f"Written weekly index: {index_path}")

    # Step 8: Send summary email
    if out_cfg.get("send_summary_email", True):
        html = generate_html_email(processed, week)
        to = out_cfg["summary_email_to"]
        subject = f"[Research Assistant] 本周文献摘要 {week}"
        recipients = ", ".join(to) if isinstance(to, list) else to
        log.info(f"Sending summary email to {recipients}...")
        try:
            send_summary_email(to, subject, html)
            log.info("Summary email sent successfully")
        except Exception as e:
            log.error(f"Failed to send summary email: {e}")

    log.info("Email extraction complete.")


if __name__ == "__main__":
    main()
