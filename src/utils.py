def create_fake_paper_text(node_id):

    topics = [
        "neural networks",
        "reinforcement learning",
        "genetic algorithms",
        "rule learning",
        "probabilistic methods",
        "deep learning",
        "graph learning"
    ]

    topic = topics[node_id % len(topics)]

    text = (
        f"Paper {node_id} discusses "
        f"{topic} and machine learning methods."
    )

    return text


def generate_all_paper_texts(num_nodes):

    paper_texts = {}

    for i in range(num_nodes):

        paper_texts[i] = create_fake_paper_text(i)

    return paper_texts