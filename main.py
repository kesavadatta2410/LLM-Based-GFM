import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.pipeline import run_pipeline

node_id = 25

result = run_pipeline(
    node_id=node_id,
    few_shot=True
)

print("\nGRAPH NARRATIVE:\n")

print(result["graph_text"])

print("\nPREDICTION:\n")

print(result["prediction"])