# DevAgent

**An extensible, multi-provider AI coding agent built with Python.**

DevAgent is a command-line AI assistant designed to help developers interact with large language models (LLMs), explore codebases, and eventually automate software development tasks through controlled tools and human approval.

The project focuses on understanding and implementing agent architecture from the ground up, including provider integrations, tool execution, human-in-the-loop workflows, code generation, and automated quality assurance.

> **Project status:** Early development. Core LLM integrations and the initial human-in-the-loop tool foundation are implemented. Advanced coding-agent capabilities are under development.

## Features

### Implemented

- Multi-provider architecture using a shared LLM interface.
- DeepSeek API integration.
- OpenAI API integration.
- Provider selection through CLI arguments.
- Environment-based configuration.
- API error handling for authentication, rate limits, connection failures, and API errors.
- Human-in-the-loop approval before executing supported actions.
- Approval-aware action executor.
- Workspace-restricted file-writing functionality with basic path traversal protection.
- Unit tests using pytest.
- Test coverage reporting using pytest-cov.

### Planned

- Claude integration (Anthropic).
- Qwen integration (Alibaba).
- Gemini integration (Google).
- File reading and directory exploration tools.
- LLM-driven tool calling.
- AI-powered code generation and modification.
- Code debugging and error analysis.
- Automated frontend and backend QA.
- API testing and browser-based testing.
- Token usage and cost tracking.
- Model routing and context optimization.
- Local model support through Ollama and Hugging Face Transformers.
- Python package distribution through PyPI.

## Supported LLM Providers

DevAgent uses a provider-based architecture so different LLM services can be integrated behind a common interface.

| Provider | Organization | Status |
|---|---|---|
| DeepSeek | DeepSeek | Implemented |
| OpenAI | OpenAI | Implemented |
| Claude | Anthropic | Planned |
| Qwen | Alibaba | Planned |
| Gemini | Google | Planned |

The goal is to switch between providers without changing the core agent logic.

## Tech Stack

- **Language:** Python
- **Package and environment management:** uv
- **LLM integration:** OpenAI Python SDK
- **Configuration:** python-dotenv
- **Testing:** pytest
- **Coverage:** pytest-cov
- **File operations:** pathlib

## Requirements

- Python 3.14 or later
- uv
- API key for the provider you want to use

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/huneshkumar/devagent.git
cd devagent
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root.

```env
# DeepSeek
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPSEEK_MODEL=deepseek-chat

# OpenAI
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=your_openai_model
```

Only configure the API key for the provider you intend to use.

**Important:** Never commit your `.env` file or expose API keys in your repository.

### 4. Run DevAgent

Using DeepSeek:

```bash
uv run python -m devagent.main --provider deepseek "Explain Python decorators"
```

Using OpenAI:

```bash
uv run python -m devagent.main --provider openai "Explain Python decorators"
```

## Project Structure

```text
devagent/
│
├── src/
│   └── devagent/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       │
│       ├── providers/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── deepseek.py
│       │   ├── openai_provider.py
│       │   └── factory.py
│       │
│       └── tools/
│           ├── __init__.py
│           ├── approval.py
│           ├── executor.py
│           └── file_tools.py
│
├── tests/
│   ├── test_approval.py
│   ├── test_deepseek.py
│   ├── test_executor.py
│   ├── test_factory.py
│   ├── test_file_tools.py
│   ├── test_main.py
│   └── test_openai_provider.py
│
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Architecture

### 1. Provider architecture

DevAgent uses a shared provider interface.

```text
              CLI
               |
               v
          Provider Factory
               |
       +-------+-------+
       |               |
       v               v
   DeepSeek           OpenAI
       |               |
       v               v
   LLM API           LLM API
       |               |
       +-------+-------+
               |
               v
          AI Response
```

Future providers such as Claude, Qwen, and Gemini will follow the same interface.

### 2. Human-in-the-loop architecture

DevAgent includes an initial approval mechanism for actions that modify files.

```text
        Requested Action
               |
               v
       Approval Request
               |
               v
        User Decision
          /       \
         /         \
      Approve     Reject
        |            |
        v            v
    Execute       Cancel
        |
        v
    Completion
```

The current file-writing tool uses this approval workflow. LLM-driven tool selection and execution are not yet integrated.

## Testing

Run the complete test suite:

```bash
uv run pytest
```

Run tests with detailed output:

```bash
uv run pytest -v
```

Run tests with coverage:

```bash
uv run pytest --cov=devagent --cov-report=term-missing
```

The current test suite covers provider selection, provider responses, CLI behavior, approval decisions, action execution, and basic file-writing security checks.

## Development Roadmap

### Phase 1: Core Foundation

- [x] Project structure and configuration.
- [x] Shared LLM provider interface.
- [x] DeepSeek integration.
- [x] OpenAI integration.
- [x] Provider factory.
- [x] CLI interface.
- [x] API error handling.
- [x] Initial automated tests.

### Phase 2: Human-in-the-Loop and Tools

- [x] Approval mechanism.
- [x] Approval-aware executor.
- [x] Initial file-writing tool.
- [x] Basic workspace path validation.
- [ ] File-reading tool.
- [ ] Directory-listing tool.
- [ ] Stronger filesystem security.
- [ ] Structured tool results and error handling.

### Phase 3: Multi-Provider Expansion

- [ ] Claude integration.
- [ ] Qwen integration.
- [ ] Gemini integration.
- [ ] Consistent provider configuration.
- [ ] Provider-specific tests.

### Phase 4: Coding Agent

- [ ] LLM-driven tool calling.
- [ ] Codebase exploration.
- [ ] AI code generation.
- [ ] Safe code modification.
- [ ] Debugging assistance.
- [ ] Human approval for risky operations.

### Phase 5: Automated QA Agent

- [ ] Frontend testing.
- [ ] Backend testing.
- [ ] API contract validation.
- [ ] Browser-based E2E testing.
- [ ] Regression testing.
- [ ] Evidence-based QA reports.

### Phase 6: Performance and Optimization

- [ ] Token usage tracking.
- [ ] API cost monitoring.
- [ ] Context optimization.
- [ ] Model routing.
- [ ] Response caching.
- [ ] Retry and execution limits.

### Phase 7: Local Models

- [ ] Ollama integration.
- [ ] Hugging Face Transformers integration.
- [ ] Qwen local models.
- [ ] Offline execution support.
- [ ] Local versus cloud model selection.

### Phase 8: Packaging and Distribution

- [ ] Finalize Python package structure.
- [ ] Configure CLI entry point.
- [ ] Build and test distribution packages.
- [ ] Publish to PyPI.
- [ ] Installation documentation.
- [ ] Usage examples and developer documentation.

## Project Goals

DevAgent is being developed with the following long-term goals:

1. Build a practical AI coding agent with a modular architecture.
2. Support multiple cloud and local LLM providers.
3. Give developers control over file modifications and risky operations.
4. Automate coding, debugging, and software quality assurance.
5. Optimize token usage, latency, and API costs.
6. Make the tool easy to install and use through a Python CLI.

## Contributing

Contributions, suggestions, and discussions are welcome.

If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

## License

A license will be selected and added before the first public release.