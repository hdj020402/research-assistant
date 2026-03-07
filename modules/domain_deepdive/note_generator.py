"""Generate Obsidian deep-dive notes for each analyzed paper."""
from pathlib import Path
from shared.file_utils import sanitize_filename, write_markdown
from modules.domain_deepdive.citation_graph import PaperNode
from modules.domain_deepdive.paper_analyzer import PaperAnalysis


def write_deepdive_note(
    order: int,
    node: PaperNode,
    analysis: PaperAnalysis,
    graph: dict[str, PaperNode],
    field_name: str,
    notes_dir: str,
    has_pdf: bool = False,
) -> Path:
    """
    Write a deep-dive Obsidian note for a single paper.
    Returns the note path.
    """
    safe_field = sanitize_filename(field_name)
    safe_title = sanitize_filename(node.title)
    filename = f"{order:03d}_{safe_title}.md"
    note_path = Path(notes_dir) / safe_field / filename

    # Build citation relationship links
    ref_links = []
    for ref_id in node.reference_ids:
        ref_node = graph.get(ref_id)
        if ref_node:
            ref_idx = _find_order(ref_id, graph)
            ref_safe = sanitize_filename(ref_node.title)
            ref_links.append(f"[[{ref_idx:03d}_{ref_safe}]]")

    cit_links = []
    for cit_id in node.citation_ids:
        cit_node = graph.get(cit_id)
        if cit_node:
            cit_idx = _find_order(cit_id, graph)
            cit_safe = sanitize_filename(cit_node.title)
            cit_links.append(f"[[{cit_idx:03d}_{cit_safe}]]")

    authors_str = ", ".join(node.authors[:5])
    if len(node.authors) > 5:
        authors_str += " et al."

    safe_title_yaml = node.title.replace('"', '\\"')
    safe_field_yaml = field_name.replace('"', '\\"')

    content = f"""---
title: "{safe_title_yaml}"
field: "{safe_field_yaml}"
order: {order}
year: {node.year or "null"}
citation_count: {node.citation_count}
has_pdf: {str(has_pdf).lower()}
doi: "{node.doi}"
url: "{node.url}"
type: deepdive-note
---

# {node.title}

**Authors**: {authors_str}
**Year**: {node.year or "N/A"} | **Citations**: {node.citation_count}

## 问题陈述
{analysis.problem}

## 方法论
{analysis.methodology}

## 关键结果
{analysis.key_results}

## 未解决问题
{analysis.open_questions}

## 在领域中的重要性
{analysis.significance}

## 摘要（英文）
{node.abstract if node.abstract else "_Abstract not available._"}

## 引用关系
- **引用了**: {", ".join(ref_links) if ref_links else "_无_"}
- **被引用**: {", ".join(cit_links) if cit_links else "_无_"}

## Links
{f"- [Full Article]({node.url})" if node.url else ""}
{f"- [Open Access PDF]({node.open_access_pdf_url})" if node.open_access_pdf_url else ""}
"""
    write_markdown(note_path, content)
    return note_path


def write_deepdive_index(
    field_name: str,
    notes_dir: str,
    graph: dict[str, PaperNode],
    ordered_ids: list[str],
    graph_file: str = "",
) -> Path:
    """Write a field-level index note."""
    safe_field = sanitize_filename(field_name)
    index_path = Path(notes_dir) / safe_field / "index.md"

    rows = []
    for i, pid in enumerate(ordered_ids, 1):
        node = graph.get(pid)
        if not node:
            continue
        safe_title = sanitize_filename(node.title)
        link = f"[[{i:03d}_{safe_title}]]"
        rows.append(
            f"| {i} | {link} | {node.year or 'N/A'} | {node.citation_count} | {node.level} |"
        )

    table_rows = "\n".join(rows)
    content = f"""---
field: "{field_name}"
type: deepdive-index
paper_count: {len(ordered_ids)}
---
# 领域深挖：{field_name}

共分析 **{len(ordered_ids)}** 篇文献。
{f"引用图谱：`{graph_file}`" if graph_file else ""}

| # | 标题 | 年份 | 引用数 | 层级 |
|---|------|------|--------|------|
{table_rows}
"""
    write_markdown(index_path, content)
    return index_path


def _find_order(paper_id: str, graph: dict[str, PaperNode]) -> int:
    """Find the 1-based index of a paper in graph (ordered by citation_count desc)."""
    sorted_ids = sorted(
        graph.keys(),
        key=lambda pid: graph[pid].citation_count,
        reverse=True,
    )
    try:
        return sorted_ids.index(paper_id) + 1
    except ValueError:
        return 0
