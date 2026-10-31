# Research Agent

A multi-agent research assistant that searches the web, extracts content from a relevant page, drafts a report, and critiques the result. Use the Streamlit interface to enter a topic and review or download the generated report.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)
- API keys for [Groq](https://console.groq.com/) and [Tavily](https://app.tavily.com/)

## Setup

From the project directory, create a `.env` file:

```dotenv
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Install the project dependencies:

```bash
uv sync
```

## Run the web app

```bash
uv run streamlit run app.py
```

Open the local URL printed by Streamlit, enter a research topic, and select **Run Research Pipeline**. The app displays search results, extracted content, a generated report, and critic feedback. You can download the report as a Markdown file.

## Run the command-line pipeline

```bash
uv run python main.py
```

The command-line entry point currently runs the sample topic defined in `main.py` and prints the pipeline output.

## Pipeline

1. **Search:** Uses Tavily to find web results.
2. **Read:** Fetches a selected result and extracts readable page content.
3. **Write:** Uses a language model through LangChain and Groq to draft a structured report.
4. **Critique:** Reviews the report and provides a score, strengths, and suggested improvements.

The research pipeline is implemented in `src/pipelines/pipeline.py`; agent and model setup is in `src/agent/agent.py`; web search and page extraction tools are in `src/tools/tools.py`.

## Notes

- Search, model generation, and page fetching require an internet connection and valid API keys.
- Page extraction depends on the selected site allowing requests; some pages may not yield usable content.
- Treat generated reports as research assistance and verify important claims against the cited sources.