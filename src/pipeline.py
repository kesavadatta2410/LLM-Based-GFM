from src.dataset_loader import (
    load_cora_dataset
)

from src.graph_builder import (
    build_graph
)

from src.text_converter import (
    graph_to_text
)

from src.prompt_builder import (
    build_prompt
)

from src.llm_client import (
    ask_llm
)

from src.utils import (
    generate_all_paper_texts
)


dataset, data = load_cora_dataset()

graph = build_graph(data)

paper_texts = generate_all_paper_texts(
    data.num_nodes
)


def run_pipeline(
    node_id,
    few_shot=False
):

    graph_text = graph_to_text(
        node_id,
        graph,
        paper_texts
    )

    if few_shot:

        prompt_path = (
            "prompts/few_shot.txt"
        )

    else:

        prompt_path = (
            "prompts/zero_shot.txt"
        )

    prompt = build_prompt(
        graph_text,
        prompt_path
    )

    prediction = ask_llm(prompt)

    return {
        "graph_text": graph_text,
        "prediction": prediction
    }