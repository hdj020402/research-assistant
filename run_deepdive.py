"""Entry point for Module 2: Domain Deep-Dive via Semantic Scholar."""
import sys
import os
import argparse
import logging
from datetime import datetime
import pytz

from shared.config_loader import load_config
from shared.claude_client import ClaudeClient
from modules.domain_deepdive.semantic_scholar import SemanticScholarClient
from modules.domain_deepdive.citation_graph import build_citation_graph
from modules.domain_deepdive.paper_analyzer import analyze_paper
from modules.domain_deepdive.graph_exporter import export_drawio_xml
from modules.domain_deepdive.note_generator import (
    write_deepdive_note,
    write_deepdive_index,
    _find_order,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Domain Deep-Dive via Semantic Scholar")
    parser.add_argument(
        "--keywords",
        required=True,
        help="Search keywords (e.g. 'graph neural network drug discovery')",
    )
    parser.add_argument(
        "--field-name",
        required=True,
        help="Field name for output directory (e.g. 'gnn-drug-discovery')",
    )
    args = parser.parse_args()

    config = load_config("config.yml")
    claude = ClaudeClient(config)

    tz = config["global"]["timezone"]
    now = datetime.now(pytz.timezone(tz))
    date_str = now.strftime("%Y%m%d")

    dd_cfg = config["domain_deepdive"]
    ss_cfg = dd_cfg["semantic_scholar"]
    traversal_cfg = ss_cfg["citation_traversal"]
    out_cfg = dd_cfg["output"]

    field_name = args.field_name
    keywords = args.keywords

    log.info(f"Starting deep-dive for field: '{field_name}'")
    log.info(f"Keywords: {keywords}")

    # Step 1: Initialize Semantic Scholar client
    ss = SemanticScholarClient(use_api_key=ss_cfg.get("use_api_key", True))

    # Step 2: Search for seed papers
    log.info("Searching Semantic Scholar for seed papers...")
    seed_raw = ss.search_papers(keywords, limit=ss_cfg["initial_search_limit"])
    log.info(f"Found {len(seed_raw)} seed papers")

    if not seed_raw:
        log.error("No papers found for the given keywords. Exiting.")
        sys.exit(1)

    for i, p in enumerate(seed_raw[:5]):
        log.info(
            f"  Seed {i+1}: {p.get('title', 'N/A')[:60]} ({p.get('year', 'N/A')}, {p.get('citationCount', 0)} cit.)"
        )

    # Step 3: Build citation graph
    log.info(
        f"Building citation graph (max_levels={traversal_cfg['max_levels']}, "
        f"min_citations={ss_cfg['min_citation_count']})..."
    )
    graph = build_citation_graph(
        seed_papers=seed_raw,
        client=ss,
        max_levels=traversal_cfg["max_levels"],
        max_papers_per_level=traversal_cfg["max_papers_per_level"],
        max_expand_per_paper=traversal_cfg["max_expand_per_paper"],
        min_citation_count=ss_cfg["min_citation_count"],
    )
    log.info(f"Citation graph built: {len(graph)} unique papers")

    # Sort by citation count descending for consistent numbering
    ordered_ids = sorted(
        graph.keys(),
        key=lambda pid: graph[pid].citation_count,
        reverse=True,
    )

    # Step 4: Optionally download open-access PDFs
    pdf_dir = out_cfg.get("pdf_dir", "output/pdfs")
    download_pdfs = out_cfg.get("download_open_access_pdf", True)
    downloaded_pdfs: set[str] = set()

    if download_pdfs:
        log.info("Downloading open-access PDFs...")
        for pid in ordered_ids:
            node = graph[pid]
            if node.open_access_pdf_url:
                safe_title = node.title[:50].replace("/", "-").replace("\\", "-")
                dest = os.path.join(pdf_dir, field_name, f"{safe_title}.pdf")
                success = ss.download_pdf({"openAccessPdf": {"url": node.open_access_pdf_url}}, dest)
                if success:
                    downloaded_pdfs.add(pid)
                    log.info(f"  Downloaded PDF: {safe_title[:40]}")

    # Step 5: Analyze papers with Claude Opus
    notes_dir = out_cfg["notes_dir"]
    log.info(f"Analyzing {len(ordered_ids)} papers with Claude Opus...")
    analyses = {}
    for i, pid in enumerate(ordered_ids):
        node = graph[pid]
        log.info(f"  [{i+1}/{len(ordered_ids)}] Analyzing: {node.title[:60]}")
        try:
            analysis = analyze_paper(node, claude)
            analyses[pid] = analysis
        except Exception as e:
            log.error(f"  Failed to analyze paper: {e}")
            from modules.domain_deepdive.paper_analyzer import PaperAnalysis
            analyses[pid] = PaperAnalysis(
                problem="Analysis failed.",
                methodology="Analysis failed.",
                key_results="Analysis failed.",
                open_questions="Analysis failed.",
                significance="Analysis failed.",
            )

    # Step 6: Write Obsidian deep-dive notes
    log.info(f"Writing deep-dive notes to {notes_dir}/{field_name}/")
    for i, pid in enumerate(ordered_ids, 1):
        node = graph[pid]
        analysis = analyses[pid]
        has_pdf = pid in downloaded_pdfs
        try:
            path = write_deepdive_note(
                order=i,
                node=node,
                analysis=analysis,
                graph=graph,
                field_name=field_name,
                notes_dir=notes_dir,
                has_pdf=has_pdf,
            )
            log.info(f"  Written: {path.name}")
        except Exception as e:
            log.error(f"  Failed to write note for '{node.title[:40]}': {e}")

    # Step 7: Export DrawIO graph
    graph_dir = out_cfg.get("graph_dir", "output/graphs")
    graph_filename = f"{field_name}_{date_str}.xml"
    graph_path = os.path.join(graph_dir, graph_filename)
    os.makedirs(graph_dir, exist_ok=True)
    log.info(f"Exporting citation graph to {graph_path}...")
    xml_content = export_drawio_xml(graph, ordered_ids, field_name)
    with open(graph_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    log.info("DrawIO XML exported successfully")

    # Step 8: Write field index note
    index_path = write_deepdive_index(
        field_name=field_name,
        notes_dir=notes_dir,
        graph=graph,
        ordered_ids=ordered_ids,
        graph_file=graph_filename,
    )
    log.info(f"Written field index: {index_path}")

    log.info(
        f"Deep-dive complete. {len(ordered_ids)} papers analyzed, "
        f"{len(downloaded_pdfs)} PDFs downloaded."
    )


if __name__ == "__main__":
    main()
