from src.config import MAX_NEIGHBORS

def graph_to_text(
    node_id,
    graph,
    paper_texts
):

    neighbors = list(
        graph.neighbors(node_id)
    )

    target_text = paper_texts[node_id]

    narrative = ""

    narrative += (
        "TARGET PAPER\n"
    )

    narrative += (
        f"Paper ID: {node_id}\n"
    )

    narrative += (
        f"Content: {target_text}\n\n"
    )

    narrative += (
        "CITATION RELATIONSHIPS\n"
    )

    if len(neighbors) == 0:

        narrative += (
            "No citation neighbors found.\n"
        )

        return narrative

    for idx, neighbor in enumerate(
        neighbors[:MAX_NEIGHBORS]
    ):

        neighbor_text = (
            paper_texts[neighbor]
        )

        narrative += (
            f"\nNeighbor {idx+1}\n"
        )

        narrative += (
            f"Paper ID: {neighbor}\n"
        )

        narrative += (
            f"Related Content: "
            f"{neighbor_text}\n"
        )

        narrative += (
            f"Relationship: "
            f"Paper {node_id} is "
            f"connected to Paper "
            f"{neighbor}\n"
        )

    return narrative