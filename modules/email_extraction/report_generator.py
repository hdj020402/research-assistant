"""Generate Obsidian notes, weekly index, and HTML summary email."""
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pytz

from shared.file_utils import sanitize_filename, write_markdown
from modules.email_extraction.claude_processor import ProcessedArticle


def _week_range(timezone: str = "Asia/Shanghai") -> str:
    """Return previous week range string like '250303-250309' (Mon-Sun)."""
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    # Monday of previous week (emails are from the past week)
    monday = now - timedelta(days=now.weekday() + 7)
    sunday = monday + timedelta(days=6)
    return f"{monday.strftime('%y%m%d')}-{sunday.strftime('%y%m%d')}"


def write_article_note(
    article: ProcessedArticle,
    notes_dir: str,
    week_range: str,
    date_added: str,
) -> Path:
    """Write a single article as an Obsidian markdown note. Returns the note path."""
    journal_dir = sanitize_filename(article.journal)
    title_file = sanitize_filename(article.title) + ".md"
    note_path = Path(notes_dir) / week_range / journal_dir / title_file

    # Escape quotes in title for YAML
    safe_title = article.title.replace('"', '\\"')
    safe_journal = article.journal.replace('"', '\\"')
    safe_title_zh = article.title_zh.replace('"', '\\"') if article.title_zh else ""
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in article.tags) + "]"

    content = f"""---
title: "{safe_title}"
title_zh: "{safe_title_zh}"
journal: "{safe_journal}"
doi: "{article.doi}"
url: "{article.url}"
pub_date: "{article.pub_date}"
tags: {tags_yaml}
ai_relevance: {article.ai_relevance}
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "{date_added}"
---

# {article.title}
{f"{chr(10)}**{article.title_zh}**{chr(10)}" if article.title_zh else ""}
{f"## 精华总结{chr(10)}{article.highlights}{chr(10)}" if article.highlights else ""}
## 摘要（英文）
{article.abstract_en if article.abstract_en else "_No abstract available._"}

## 摘要（中文）
{article.abstract_zh if article.abstract_zh else "_翻译失败_"}

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article]({article.url})
"""
    write_markdown(note_path, content)
    return note_path


def write_weekly_index(
    notes_dir: str,
    week_range: str,
    article_count: int,
) -> Path:
    """Write the weekly index file with Dataview query."""
    index_path = Path(notes_dir) / week_range / "index.md"
    content = f"""---
week: "{week_range}"
type: weekly-index
article_count: {article_count}
---
# 本周文献 ({week_range})

共收录 **{article_count}** 篇文章。

```dataview
TABLE title, journal, ai_relevance, read_status, tags
FROM "Paper/{week_range}"
WHERE type = "paper-note"
SORT ai_relevance DESC
```
"""
    write_markdown(index_path, content)
    return index_path


def generate_html_email(
    articles: list[ProcessedArticle],
    week_range: str,
) -> str:
    """Generate an HTML summary email sorted by ai_relevance descending."""
    sorted_articles = sorted(articles, key=lambda a: a.ai_relevance, reverse=True)

    cards = ""
    for i, a in enumerate(sorted_articles, 1):
        tags_html = " ".join(
            f'<span style="background:#e8f4fd;color:#1a73e8;padding:2px 6px;border-radius:3px;font-size:11px;display:inline-block;margin:2px 2px 2px 0;">{t}</span>'
            for t in a.tags
        )
        stars = "★" * a.ai_relevance + "☆" * (5 - a.ai_relevance)
        cards += f"""
    <div style="border:1px solid #e0e0e0;border-radius:8px;padding:16px;margin-bottom:14px;background:#fff;">
      <div style="margin-bottom:8px;">
        <span style="color:#f5a623;font-size:15px;margin-right:8px;" title="AI相关度 {a.ai_relevance}/5">{stars}</span>
        <span style="color:#888;font-size:12px;">{_escape_html(a.journal)}{f' · {a.pub_date}' if a.pub_date else ''}</span>
        <span style="color:#999;font-size:12px;float:right;">#{i}</span>
      </div>
      <div style="margin-bottom:6px;">
        <a href="{a.url}" style="color:#1a0dab;text-decoration:none;font-size:15px;font-weight:bold;line-height:1.4;">{_escape_html(a.title)}</a>
      </div>
      {f'<div style="color:#555;font-size:13px;margin-bottom:6px;">{_escape_html(a.title_zh)}</div>' if a.title_zh else ""}
      {f'<div style="color:#888;font-size:11px;margin-bottom:8px;">{_escape_html(a.authors)}</div>' if a.authors else ""}
      {f'<div style="background:#f0f7ff;border-left:3px solid #1a73e8;padding:8px 10px;margin-bottom:8px;font-size:13px;color:#1a73e8;border-radius:0 4px 4px 0;">{_escape_html(a.highlights)}</div>' if a.highlights else ""}
      <div style="font-size:13px;color:#333;line-height:1.6;margin-bottom:8px;">{_escape_html(a.abstract_zh)}</div>
      <details style="margin-bottom:8px;">
        <summary style="font-size:12px;color:#888;cursor:pointer;">English abstract</summary>
        <p style="font-size:12px;color:#555;line-height:1.5;margin-top:6px;">{_escape_html(a.abstract_en)}</p>
      </details>
      <div>{tags_html}</div>
    </div>
"""

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>文献周报 {week_range}</title></head>
<body style="font-family:Arial,sans-serif;max-width:760px;margin:0 auto;padding:20px;color:#333;background:#f5f5f5;">
  <h1 style="color:#2c3e50;border-bottom:2px solid #3498db;padding-bottom:10px;">
    文献周报 ({week_range})
  </h1>
  <p style="color:#666;">共 <strong>{len(articles)}</strong> 篇文章，按 AI 相关度排序</p>
  {cards}
  <p style="color:#888;font-size:12px;margin-top:20px;text-align:center;">
    由 Research Assistant 自动生成 · {week_range}
  </p>
</body>
</html>"""
    return html


def _escape_html(text: str) -> str:
    """Escape HTML special characters."""
    if not text:
        return ""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
