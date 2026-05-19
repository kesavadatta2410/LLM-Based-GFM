# LLM-Based Graph Foundation Model

This project demonstrates how to use Large Language Models as Graph Foundation Models through Natural Language Conversion.

## Features

- **Cora citation graph** - Loads the Cora dataset for citation network analysis
- **Graph-to-text conversion** - Transforms graph structures into natural language narratives
- **Zero-shot prompting** - Direct classification without examples
- **Few-shot prompting** - Classification with example demonstrations
- **LLM-based node classification** - Uses Grok API for paper category prediction
- **Streamlit deployment** - Interactive web interface

## Installation

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
```

## Configuration

Create a `.env` file with your API key:

```
GROK_API_KEY=your_api_key_here
```

## Usage

```bash
streamlit run app/app.py
```

## Project Structure

```
├── app/
│   └── app.py              # Streamlit web interface
├── data/                   # Cora dataset (auto-downloaded)
├── prompts/
│   ├── few_shot.txt        # Few-shot prompt template
│   └── zero_shot.txt       # Zero-shot prompt template
├── src/
│   ├── config.py           # Configuration and environment variables
│   ├── dataset_loader.py   # Cora dataset loading
│   ├── graph_builder.py    # Graph construction
│   ├── llm_client.py       # LLM API client
│   ├── pipeline.py         # Main pipeline orchestration
│   ├── prompt_builder.py   # Prompt generation
│   ├── text_converter.py   # Graph-to-text conversion
│   └── utils.py            # Utility functions
└── README.md
```

## License

MIT