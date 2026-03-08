# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Summary

Research assistant toolkit for a chemistry researcher (AI for Chemistry domain). Two independent modules that fetch academic papers, analyze them with Claude, and output Obsidian-compatible markdown notes.

## Running

```bash
# Install dependencies
pip install -r requirements.txt

# Module 1: Email extraction (weekly journal ToC → Obsidian notes + summary email)
python run_email.py

# Module 2: Domain deep-dive (Semantic Scholar → citation graph → analyzed notes)
python run_deepdive.py --keywords "graph neural network drug discovery" --field-name "gnn-drug-discovery"

# One-time Gmail OAuth setup (requires client_secret.json from Google Cloud Console)
pip install google-auth-oauthlib
python scripts/get_gmail_token.py
```

No tests, no linter, no build step. Python 3.11, plain scripts.

## Required Environment Variables

- `ANTHROPIC_API_KEY` (both modules) — optionally `ANTHROPIC_BASE_URL` for proxy
- `GMAIL_CLIENT_ID`, `GMAIL_CLIENT_SECRET`, `GMAIL_REFRESH_TOKEN` (Module 1)
- `SEMANTIC_SCHOLAR_API_KEY` (Module 2)

## Architecture

**Two modules, shared utilities, zero interdependency between modules.**

### Module 1: Email Extraction (`run_email.py`)
Pipeline: Gmail ToC emails → `email_parser.py` (HTML parsing, section-aware filtering) → `abstract_fetcher.py` (scrape publisher pages) → keyword pre-filter from `config.yml` → `claude_processor.py` (Haiku: translate, tag, score) → `report_generator.py` (Obsidian notes + HTML email) → send via Gmail.

### Module 2: Domain Deep-Dive (`run_deepdive.py`)
Pipeline: Semantic Scholar keyword search → `citation_graph.py` (BFS traversal, 2-level default) → `paper_analyzer.py` (Opus: deep analysis) → `note_generator.py` (Obsidian notes with `[[wikilinks]]`) + `graph_exporter.py` (DrawIO XML).

### Shared (`shared/`)
- `claude_client.py` — wraps Anthropic SDK; `.haiku()` for fast tasks, `.opus()` for deep analysis
- `config_loader.py` — loads `config.yml`, reads secrets from env vars
- `rate_limiter.py` — token-bucket limiter, used as decorator or via `.wait()`
- `file_utils.py` — `sanitize_filename()`, `write_markdown()`

## Key Conventions

- All configuration in `config.yml` — model names, sender patterns, relevance keywords, traversal params, output dirs
- Claude API calls always return JSON-only responses; parsers strip markdown code blocks as fallback
- Rate limiting on all external APIs: Claude (0.5 req/s Haiku, 0.3 req/s Opus), Semantic Scholar (0.3-0.9 req/s), publisher pages (0.5 req/s)
- Notes output to `notes/daily/{YYMMDD-YYMMDD}/{Journal}/` (Module 1) and `notes/deepdive/{field-name}/` (Module 2)
- Obsidian note frontmatter uses `type: paper-note` / `deepdive-note` for Dataview queries
- Chinese translations and section headers throughout (user is a Chinese researcher)

## GitHub Actions

- `email_extraction.yml` — scheduled weekly (Monday 08:00 UTC / 16:00 Beijing), auto-commits notes
- `domain_deepdive.yml` — manual trigger (`workflow_dispatch`) with `field_keywords` and `field_name` inputs
- `verify_secrets.yml` — validates required secrets are set

## Data Flow Boundaries

- `email_parser.py` handles publisher-specific HTML parsing (ACS, Nature, RSC, Elsevier, Wiley, Springer) with section-aware filtering and multiple extraction strategies (DOI links → link-text → plain-text fallback)
- `abstract_fetcher.py` has per-publisher CSS selectors with generic fallback
- `config.yml` `relevance_keywords` list controls the keyword pre-filter that runs before Claude to save tokens
