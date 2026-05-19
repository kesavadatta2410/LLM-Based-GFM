def load_prompt_template(path):

    with open(path, "r") as f:

        template = f.read()

    return template


def build_prompt(
    graph_text,
    prompt_path
):

    template = load_prompt_template(
        prompt_path
    )

    prompt = template.format(
        graph_text=graph_text
    )

    return prompt