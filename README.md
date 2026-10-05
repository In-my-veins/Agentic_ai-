# Tuto Agentic AI

A collection of learning notebooks and small applications for exploring agentic AI, language models, retrieval augmented generation, multimodal input, and vector databases.

## Contents

- `2_Health_analysis/` — health document analysis notebook (the private sample document is not included)
- `gemini_models/` — Gemini model experiments
- `Multi_modal/` — multimodal model experiments
- `RAG/` — retrieval augmented generation notebook
- `simple_llm_calling/` — basic language model calls
- `Single_agent/` — single-agent product query examples
- `Streamlit_app/` — Streamlit example app
- `Vector_db/` — vector database learning notebook
- `src/` — Python package scaffold

Notebook outputs were cleared in the published copies. Some examples need provider API keys; store them in a local `.env` file and never commit that file.

## Setup

The project uses Python 3.14 and `uv`:

```bash
uv sync
```

To run a notebook:

```bash
uv run jupyter lab
```

To start the Streamlit example:

```bash
uv run streamlit run Streamlit_app/app.py
```
