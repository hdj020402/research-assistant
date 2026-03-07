"""Generate Obsidian notes, weekly index, and HTML summary email."""
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pytz

from shared.file_utils import sanitize_filename, write_markdown
from modules.email_extraction.claude_processor import ProcessedArticle


def _week_range(timezone: str = "Asia/Shanghai") -> str:
    """Return current week range string like '250303-250309' (Mon-Sun)."""
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    # Monday of current week
    monday = now - timedelta(days=now.weekday())
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
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in article.tags) + "]"

    content = f"""---
title: "{safe_title}"
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

    rows = ""
    for i, a in enumerate(sorted_articles, 1):
        tags_html = " ".join(
            f'<span style="background:#e8f4fd;color:#1a73e8;padding:2px 6px;border-radius:3px;font-size:11px;">{t}</span>'
            for t in a.tags
        )
        stars = "★" * a.ai_relevance + "☆" * (5 - a.ai_relevance)
        rows += f"""
        <tr style="border-bottom:1px solid #e0e0e0;">
          <td style="padding:12px 8px;font-weight:bold;color:#666;width:40px;">{i}</td>
          <td style="padding:12px 8px;">
            <a href="{a.url}" style="color:#1a0dab;text-decoration:none;font-weight:bold;">{_escape_html(a.title)}</a>
            <br><span style="color:#888;font-size:12px;">{_escape_html(a.journal)} · {a.pub_date}</span>
            {f'<br><span style="color:#888;font-size:11px;">{_escape_html(a.authors)}</span>' if a.authors else ""}
          </td>
          <td style="padding:12px 8px;width:60px;color:#f5a623;font-size:16px;" title="AI相关度 {a.ai_relevance}/5">{stars}</td>
          <td style="padding:12px 8px;max-width:400px;">
            <p style="margin:0 0 6px;font-size:13px;color:#333;">{_escape_html(a.abstract_zh)}</p>
            <details>
              <summary style="font-size:12px;color:#888;cursor:pointer;">English abstract</summary>
              <p style="font-size:12px;color:#555;">{_escape_html(a.abstract_en)}</p>
            </details>
            <div style="margin-top:6px;">{tags_html}</div>
          </td>
        </tr>
"""

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>本周文献摘要 {week_range}</title></head>
<body style="font-family:Arial,sans-serif;max-width:900px;margin:0 auto;padding:20px;color:#333;">
  <h1 style="color:#2c3e50;border-bottom:2px solid #3498db;padding-bottom:10px;">
    本周文献摘要 ({week_range})
  </h1>
  <p style="color:#666;">共 <strong>{len(articles)}</strong> 篇文章，按 AI 相关度排序</p>
  <table style="width:100%;border-collapse:collapse;">
    <thead>
      <tr style="background:#f8f9fa;border-bottom:2px solid #dee2e6;">
        <th style="padding:10px 8px;text-align:left;">#</th>
        <th style="padding:10px 8px;text-align:left;">标题</th>
        <th style="padding:10px 8px;text-align:left;">AI相关度</th>
        <th style="padding:10px 8px;text-align:left;">摘要</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
  <p style="color:#888;font-size:12px;margin-top:20px;">
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
