# LLM-Based Graph Foundation Model

A framework demonstrating how Large Language Models can serve as Graph Foundation Models through natural language conversion of graph structures.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
</p>

## Overview

This project transforms graph structures (citation networks) into natural language narratives, enabling LLM-based node classification without traditional graph neural networks. The approach converts graph topology and node features into text prompts that LLMs can process.

## Features

| Feature | Description |
|---------|-------------|
| **Graph-to-Text Conversion** | Transforms citation graph neighbors into fluent narrative |
| **Zero-Shot Classification** | Direct prediction without training examples |
| **Few-Shot Learning** | Leverages examples for improved accuracy |
| **Streamlit Interface** | Interactive web UI for real-time predictions |
| **Cora Dataset Support** | Built-in loading of citation network benchmark |

## Installation

```bash
# Clone the repository
git clone https://github.com/kesavadatta2410/LLM-Based-GFM.git
cd LLM-Based-GFM

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

## Usage

### Web Interface

```bash
streamlit run app/app.py
```

Navigate to `http://localhost:8501` and enter a node ID to classify.

### Python API

```python
from src.pipeline import run_pipeline

result = run_pipeline(node_id=25, few_shot=True)
print(result["prediction"])
```

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Cora Data  │────▶│  Graph Build  │────▶│  Text Convert   │
└─────────────┘     └──────────────┘     └─────────────────┘
                                                │
                                                ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Prompt     │◀────│  Templates   │◀────│  Graph Text     │
│  Builder    │     │ (few/zero)   │     │ (narrative)     │
└─────────────┘     └──────────────┘     └─────────────────┘
      │
      ▼
┌─────────────┐
│    LLM      │
│ (Gemini API) │
└─────────────┘
      │
      ▼
┌─────────────┐
│ Prediction  │
│ (category)  │
└─────────────┘
```

## Project Structure

```
├── app/
│   ├── app.py           # Streamlit web interface
│   └── ui_helpers.py    # UI utility functions
├── data/                # Cora dataset (auto-downloaded)
├── prompts/
│   ├── few_shot.txt     # Few-shot prompt template
│   └── zero_shot.txt    # Zero-shot prompt template
├── src/
│   ├── config.py        # Environment configuration
│   ├── dataset_loader.py # Cora dataset loader
│   ├── graph_builder.py # NetworkX graph construction
│   ├── llm_client.py    # Google Generative AI client
│   ├── pipeline.py      # Main orchestration pipeline
│   ├── prompt_builder.py # Prompt template processing
│   ├── text_converter.py # Graph-to-narrative conversion
│   └── utils.py         # Helper functions
├── main.py              # CLI entry point
├── requirements.txt     # Python dependencies
└── README.md
```

## Pipeline Overview

1. **Load Dataset**: Download Cora citation network via PyTorch Geometric
2. **Build Graph**: Convert edge index to NetworkX graph structure
3. **Generate Texts**: Create synthetic paper content for each node
4. **Convert to Narrative**: Transform node + neighbors into text format
5. **Query LLM**: Send prompt through Google Generative AI API for classification
6. **Return Prediction**: Extract predicted academic category

## License

MIT License - see [LICENSE](LICENSE) file for details.