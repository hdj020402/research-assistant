"""Entry point for Module 1: Email Journal Abstract Extraction."""
import sys
import logging
from datetime import datetime
import pytz

from shared.config_loader import load_config
from shared.claude_client import ClaudeClient
from modules.email_extraction.gmail_client import fetch_toc_emails, send_summary_email
from modules.email_extraction.email_parser import parse_email
from modules.email_extraction.abstract_fetcher import fetch_abstract
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

    # Step 3: Optionally fetch web abstracts
    if proc_cfg.get("fetch_web_abstract", True):
        timeout = proc_cfg.get("web_fetch_timeout_seconds", 10)
        for i, article in enumerate(all_articles_raw):
            if article.url and not article.abstract_from_email:
                fetched = fetch_abstract(article.url, timeout=timeout)
                if fetched:
                    article.abstract_from_email = fetched
                    log.info(f"  [{i+1}/{len(all_articles_raw)}] Fetched abstract for: {article.title[:50]}")

    # Step 4: Claude processing
    processed = []
    log.info("Processing articles with Claude Haiku...")
    for i, article in enumerate(all_articles_raw):
        log.info(f"  [{i+1}/{len(all_articles_raw)}] Processing: {article.title[:60]}")
        try:
            result = process_article(
                title=article.title,
                abstract=article.abstract_from_email,
                journal=article.journal,
                doi=article.doi,
                url=article.url,
                authors="",
                pub_date="",
                claude=claude,
            )
            processed.append(result)
        except Exception as e:
            log.error(f"  Failed to process article: {e}")

    log.info(f"Successfully processed {len(processed)} articles")

    # Step 5: Write Obsidian notes
    notes_dir = out_cfg["notes_dir"]
    log.info(f"Writing Obsidian notes to {notes_dir}/{week}/")
    for article in processed:
        try:
            path = write_article_note(article, notes_dir, week, date_added)
            log.info(f"  Written: {path.name}")
        except Exception as e:
            log.error(f"  Failed to write note for '{article.title[:40]}': {e}")

    # Step 6: Write weekly index
    index_path = write_weekly_index(notes_dir, week, len(processed))
    log.info(f"Written weekly index: {index_path}")

    # Step 7: Send summary email
    if out_cfg.get("send_summary_email", True):
        html = generate_html_email(processed, week)
        to = out_cfg["summary_email_to"]
        subject = f"[Research Assistant] 本周文献摘要 {week}"
        log.info(f"Sending summary email to {to}...")
        try:
            send_summary_email(to, subject, html)
            log.info("Summary email sent successfully")
        except Exception as e:
            log.error(f"Failed to send summary email: {e}")

    log.info("Email extraction complete.")


if __name__ == "__main__":
    main()
