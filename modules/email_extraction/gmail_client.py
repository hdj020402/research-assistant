"""Gmail OAuth2 client for reading journal ToC emails and sending summary emails."""
import os
import base64
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from typing import Optional

import pytz
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


def _build_service():
    """Build Gmail API service using OAuth2 credentials from environment."""
    creds = Credentials(
        token=None,
        refresh_token=os.environ["GMAIL_REFRESH_TOKEN"],
        client_id=os.environ["GMAIL_CLIENT_ID"],
        client_secret=os.environ["GMAIL_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/gmail.modify"],
    )
    # Force token refresh
    creds.refresh(Request())
    return build("gmail", "v1", credentials=creds)


def fetch_toc_emails(
    sender_patterns: list[str],
    subject_patterns: list[str],
    lookback_days: int = 8,
    timezone: str = "Asia/Shanghai",
) -> list[dict]:
    """
    Fetch journal ToC emails from Gmail.

    Returns a list of dicts with keys: id, sender, subject, date, html_body, text_body.
    """
    service = _build_service()
    tz = pytz.timezone(timezone)
    cutoff = datetime.now(tz) - timedelta(days=lookback_days)
    after_epoch = int(cutoff.timestamp())

    # Build query: match any sender OR subject pattern
    sender_query = " OR ".join(f"from:{s}" for s in sender_patterns)
    subject_query = " OR ".join(f'subject:"{s}"' for s in subject_patterns)
    query = f"({sender_query}) ({subject_query}) after:{after_epoch}"

    results = (
        service.users()
        .messages()
        .list(userId="me", q=query, maxResults=100)
        .execute()
    )
    messages = results.get("messages", [])

    emails = []
    for msg_ref in messages:
        msg = (
            service.users()
            .messages()
            .get(userId="me", id=msg_ref["id"], format="full")
            .execute()
        )
        parsed = _parse_message(msg)
        if parsed:
            emails.append(parsed)

    return emails


def _parse_message(msg: dict) -> Optional[dict]:
    """Extract id, sender, subject, date, html_body, text_body from raw Gmail message."""
    headers = {h["name"]: h["value"] for h in msg["payload"].get("headers", [])}
    html_body = ""
    text_body = ""
    _extract_parts(msg["payload"], html_body_holder := [], text_body_holder := [])
    html_body = "".join(html_body_holder)
    text_body = "".join(text_body_holder)

    return {
        "id": msg["id"],
        "sender": headers.get("From", ""),
        "subject": headers.get("Subject", ""),
        "date": headers.get("Date", ""),
        "html_body": html_body,
        "text_body": text_body,
    }


def _extract_parts(payload: dict, html_parts: list, text_parts: list) -> None:
    """Recursively extract text/html and text/plain parts."""
    mime_type = payload.get("mimeType", "")
    if mime_type == "text/html":
        data = payload.get("body", {}).get("data", "")
        if data:
            html_parts.append(base64.urlsafe_b64decode(data).decode("utf-8", errors="replace"))
    elif mime_type == "text/plain":
        data = payload.get("body", {}).get("data", "")
        if data:
            text_parts.append(base64.urlsafe_b64decode(data).decode("utf-8", errors="replace"))
    for part in payload.get("parts", []):
        _extract_parts(part, html_parts, text_parts)


def send_summary_email(to: str, subject: str, html_content: str) -> None:
    """Send an HTML summary email via Gmail API."""
    service = _build_service()
    msg = MIMEMultipart("alternative")
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(html_content, "html", "utf-8"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    service.users().messages().send(userId="me", body={"raw": raw}).execute()
