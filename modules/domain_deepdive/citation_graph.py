"""Build citation graph via breadth-first traversal of Semantic Scholar."""
from dataclasses import dataclass, field
from typing import Optional
from modules.domain_deepdive.semantic_scholar import SemanticScholarClient


@dataclass
class PaperNode:
    paper_id: str
    title: str
    year: Optional[int]
    citation_count: int
    abstract: str
    authors: list[str]
    doi: str
    url: str
    open_access_pdf_url: str
    reference_ids: list[str] = field(default_factory=list)   # papers this paper cites
    citation_ids: list[str] = field(default_factory=list)    # papers that cite this paper
    level: int = 0  # depth from seed papers


def build_citation_graph(
    seed_papers: list[dict],
    client: SemanticScholarClient,
    max_levels: int = 2,
    max_papers_per_level: int = 15,
    max_expand_per_paper: int = 10,
    min_citation_count: int = 10,
) -> dict[str, PaperNode]:
    """
    BFS traversal of citation graph starting from seed papers.

    Returns a dict mapping paper_id -> PaperNode.
    """
    graph: dict[str, PaperNode] = {}
    # Queue entries: (paper_dict, level)
    queue: list[tuple[dict, int]] = [(p, 0) for p in seed_papers]
    visited: set[str] = set()

    while queue:
        paper_dict, level = queue.pop(0)
        paper_id = paper_dict.get("paperId")
        if not paper_id or paper_id in visited:
            continue
        if paper_dict.get("citationCount", 0) < min_citation_count and level > 0:
            continue

        visited.add(paper_id)
        node = _make_node(paper_dict, level)
        graph[paper_id] = node

        if level >= max_levels:
            continue

        # Fetch references (papers this paper cites — upstream ancestors)
        try:
            refs = client.get_references(paper_id, limit=max_expand_per_paper * 2)
            refs_filtered = _filter_and_sort(refs, min_citation_count, max_expand_per_paper)
            for ref in refs_filtered:
                ref_id = ref.get("paperId")
                if ref_id and ref_id not in visited:
                    node.reference_ids.append(ref_id)
                    queue.append((ref, level + 1))
        except Exception:
            pass

        # Fetch citations (papers that cite this — downstream successors)
        try:
            cits = client.get_citations(paper_id, limit=max_expand_per_paper * 2)
            cits_filtered = _filter_and_sort(cits, min_citation_count, max_expand_per_paper)
            for cit in cits_filtered:
                cit_id = cit.get("paperId")
                if cit_id and cit_id not in visited:
                    node.citation_ids.append(cit_id)
                    queue.append((cit, level + 1))
        except Exception:
            pass

        # Enforce per-level paper limit
        at_this_level = sum(1 for n in graph.values() if n.level == level)
        if at_this_level >= max_papers_per_level and level == 0:
            break

    return graph


def _filter_and_sort(papers: list[dict], min_citations: int, limit: int) -> list[dict]:
    """Filter by min citations and take top N by citation count."""
    filtered = [p for p in papers if p.get("citationCount", 0) >= min_citations]
    filtered.sort(key=lambda p: p.get("citationCount", 0), reverse=True)
    return filtered[:limit]


def _make_node(paper: dict, level: int) -> PaperNode:
    """Convert a Semantic Scholar paper dict to a PaperNode."""
    authors = [a.get("name", "") for a in paper.get("authors", [])]
    doi = (paper.get("externalIds") or {}).get("DOI", "")
    pdf_url = (paper.get("openAccessPdf") or {}).get("url", "")
    return PaperNode(
        paper_id=paper.get("paperId", ""),
        title=paper.get("title", "Unknown Title"),
        year=paper.get("year"),
        citation_count=paper.get("citationCount", 0),
        abstract=paper.get("abstract") or "",
        authors=authors,
        doi=doi,
        url=paper.get("url") or (f"https://doi.org/{doi}" if doi else ""),
        open_access_pdf_url=pdf_url,
        level=level,
    )
