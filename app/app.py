import streamlit as st

from src.pipeline import run_pipeline

st.set_page_config(
    page_title="LLM Graph Foundation Model",
    layout="wide"
)

st.title(
    "LLM-Based Graph Foundation Model"
)

st.write(
    "Natural Language Graph Classification"
)

node_id = st.number_input(
    "Enter Node ID",
    min_value=0,
    max_value=2707,
    value=25
)

few_shot = st.checkbox(
    "Use Few-Shot Prompting",
    value=True
)

if st.button("Run Prediction"):

    result = run_pipeline(
        node_id=node_id,
        few_shot=few_shot
    )

    st.subheader(
        "Graph Narrative"
    )

    st.text_area(
        "Narrative",
        result["graph_text"],
        height=300
    )

    st.subheader(
        "Predicted Category"
    )

    st.success(
        result["prediction"]
    )