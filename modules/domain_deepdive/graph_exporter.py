"""Export citation graph as DrawIO-compatible XML."""
import xml.etree.ElementTree as ET
from modules.domain_deepdive.citation_graph import PaperNode


def export_drawio_xml(
    graph: dict[str, PaperNode],
    ordered_ids: list[str],
    field_name: str,
) -> str:
    """
    Generate a DrawIO-compatible XML string from the citation graph.

    Layout: papers arranged in rows by level (depth), with edges showing citation relationships.
    """
    mxfile = ET.Element("mxfile")
    diagram = ET.SubElement(mxfile, "diagram", name=field_name)
    mxgraph = ET.SubElement(
        diagram,
        "mxGraphModel",
        dx="1422",
        dy="762",
        grid="1",
        gridSize="10",
        guides="1",
        tooltips="1",
        connect="1",
        arrows="1",
        fold="1",
        page="1",
        pageScale="1",
        pageWidth="1169",
        pageHeight="827",
        math="0",
        shadow="0",
    )
    root = ET.SubElement(mxgraph, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    # Group nodes by level for layout
    levels: dict[int, list[str]] = {}
    for pid, node in graph.items():
        lv = node.level
        levels.setdefault(lv, []).append(pid)

    # Sort each level by citation count descending
    for lv in levels:
        levels[lv].sort(
            key=lambda pid: graph[pid].citation_count, reverse=True
        )

    node_cells: dict[str, str] = {}  # paper_id -> cell_id
    cell_counter = 2

    # Position constants
    X_SPACING = 200
    Y_SPACING = 120
    NODE_WIDTH = 180
    NODE_HEIGHT = 60

    for lv, pids in sorted(levels.items()):
        y = lv * Y_SPACING + 40
        for col, pid in enumerate(pids):
            node = graph[pid]
            x = col * X_SPACING + 40
            cell_id = str(cell_counter)
            node_cells[pid] = cell_id
            cell_counter += 1

            # Color by level: level 0 = gold, level 1 = light blue, level 2+ = white
            if lv == 0:
                style = (
                    "rounded=1;whiteSpace=wrap;html=1;"
                    "fillColor=#FFD700;strokeColor=#b85450;fontStyle=1;fontSize=10;"
                )
            elif lv == 1:
                style = (
                    "rounded=1;whiteSpace=wrap;html=1;"
                    "fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=9;"
                )
            else:
                style = (
                    "rounded=1;whiteSpace=wrap;html=1;"
                    "fillColor=#f5f5f5;strokeColor=#666666;fontSize=9;"
                )

            label = _truncate(node.title, 60)
            if node.year:
                label += f"\n({node.year}, {node.citation_count} cit.)"

            cell = ET.SubElement(
                root,
                "mxCell",
                id=cell_id,
                value=label,
                style=style,
                vertex="1",
                parent="1",
                tooltip=node.abstract[:200] if node.abstract else "",
            )
            ET.SubElement(
                cell,
                "mxGeometry",
                x=str(x),
                y=str(y),
                width=str(NODE_WIDTH),
                height=str(NODE_HEIGHT),
                **{"as": "geometry"},
            )

    # Add edges for citation relationships
    for pid, node in graph.items():
        src_cell = node_cells.get(pid)
        if not src_cell:
            continue
        # Edges: this paper → references (paper cites reference)
        for ref_id in node.reference_ids:
            tgt_cell = node_cells.get(ref_id)
            if tgt_cell:
                edge_id = str(cell_counter)
                cell_counter += 1
                edge = ET.SubElement(
                    root,
                    "mxCell",
                    id=edge_id,
                    style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;"
                    "jettySize=auto;exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
                    "entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
                    edge="1",
                    source=src_cell,
                    target=tgt_cell,
                    parent="1",
                )
                ET.SubElement(edge, "mxGeometry", relative="1", **{"as": "geometry"})

    xml_str = ET.tostring(mxfile, encoding="unicode", xml_declaration=False)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str


def _truncate(text: str, max_len: int) -> str:
    return text if len(text) <= max_len else text[: max_len - 3] + "..."
