# DevAgent CLI

**A multi-LLM terminal assistant for developers, built with Python.**

DevAgent CLI is an open-source project exploring how to build an AI-powered developer assistant that runs directly in the terminal. It is designed to support multiple LLM providers through a modular architecture, starting with DeepSeek and OpenAI.

The long-term goal is to build an AI coding agent that can understand codebases, assist with debugging, modify files, execute tests, and help developers automate everyday programming tasks.

> **Project status:** Early development. Currently building the foundation for multi-LLM support.

## Features

### Current capabilities
- Terminal-based interaction with an LLM.
- Support for DeepSeek and OpenAI API providers.
- Provider selection through command-line arguments.
- Environment-based API key configuration.
- Modular Python architecture.

### Planned features
- [ ] Streaming responses in the terminal.
- [ ] Interactive chat sessions.
- [ ] Codebase exploration and file search.
- [ ] Context-aware code explanations.
- [ ] AI-powered code generation and editing.
- [ ] Automated debugging and test execution.
- [ ] Tool calling and agent execution loops.
- [ ] Human approval for potentially risky operations.
- [ ] Support for additional cloud and local LLM providers.

## Tech Stack

- **Language:** Python
- **Package management:** uv
- **LLM integration:** OpenAI Python SDK
- **Supported providers:** DeepSeek, OpenAI,kimi,claude
- **Configuration:** python-dotenv
- **Interface:** Command-line interface (CLI)

## Getting Started

### Prerequisites

- Python 3.12 or a compatible version supported by the project dependencies.
- [uv](https://docs.astral.sh/uv/) installed.
- An API key for DeepSeek or OpenAI.

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd devagent
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```dotenv
MISTRAL_API_KEY= MISTEAL KEY
MISTRAL_MODEL=
XAI_API_KEY=your_XAI_api_key
XAI_MODEL=
DEEPSEEK_API_KEY=
DEEPSEEK_MODAL=
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=your_supported_model_id

```

Only configure the credentials for the provider you intend to use. Set `OPENAI_MODEL` to a model ID available to your OpenAI API account.

**Security:** Never commit API keys or your `.env` file to version control.

### 4. Run DevAgent

Use DeepSeek:

```bash
uv run python -m devagent.main --provider deepseek "Explain Python decorators"
```

Use OpenAI:

```bash
uv run python -m devagent.main --provider openai "Explain Python decorators"
```

The default provider is DeepSeek, so you can also run:

```bash
uv run python -m devagent.main "Explain how REST APIs work"
```

## Project Structure

```text
devagent/
├── src/
│   └── devagent/
│       ├── __init__.py
│       ├── main.py
│       └── providers.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

- `main.py`: Handles command-line arguments and application execution.
- `providers.py`: Configures LLM clients and sends prompts to the selected provider.
- `pyproject.toml`: Defines project metadata and dependencies.
- `uv.lock`: Records resolved dependency versions for reproducible environments.

## Architecture

DevAgent separates its command-line interface from its LLM provider implementation.

```text
User Prompt
    |
    v
Command-Line Interface
    |
    v
Provider Selection
    |
    +------> CLAUDE API
    |
    +------> OpenAI API
    |
    +------> DEEPSEEK API
    v
Generated Response
    |
    v
Terminal Output
```

This separation provides a foundation for adding new providers and agent capabilities without rewriting the entire application.

## Roadmap

**Phase 1: Multi-LLM foundation**
- Establish the project structure.
- Integrate OpenAI, DeepSeek and Kimmi.
- Configure provider selection.
- Handle API errors.

**Phase 2: Developer assistant**
- Add interactive conversations.
- Introduce streaming responses.
- Add file reading and code search.
- Improve terminal output.

**Phase 3: Agentic coding capabilities**
- Implement tool calling.
- Build an agent execution loop.
- Add controlled file editing.
- Run tests and analyze failures.
- Introduce safety controls and approval workflows.

**Phase 4: Open-source release**
- Add automated tests and CI.
- Improve installation and configuration.
- Document architecture and supported models.
- Benchmark performance across providers.

## Contributing

Contributions, suggestions, bug reports, and feature requests are welcome as the project evolves.

If you would like to contribute, open an issue to discuss the proposed change or submit a pull request.

## Learning Goals

This project is also a practical exploration of:

- LLM APIs and provider abstraction.
- Python CLI application development.
- Agentic AI architecture and tool calling.
- Codebase understanding and automated debugging.
- Secure and reliable AI-assisted software development.

## License


---

**DevAgent CLI** — Building toward a flexible, multi-LLM AI coding assistant, one step at a time.
