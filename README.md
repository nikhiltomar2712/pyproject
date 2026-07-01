# 🤖 AI Chatbot (pyproject)

[![GitHub repository](https://img.shields.io/badge/Repository-pyproject-blue?style=for-the-badge&logo=github)](https://github.com/nikhiltomar2712/pyproject)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](./LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Tests Status](https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge&logo=pytest)](./tests)

A professional, fully modular, and production-ready terminal-based AI Chatbot codebase. This project features database logging, conversational sliding-window memory buffers, crude NLP/sentiment routing, and full unit test coverage.

---

## ✨ Features

- **Modular Architecture**: Structured under the standard python source layout (`src/`).
- **Connection Context Management**: SQLite history logging with robust context manager transactional safety.
- **Sliding-Window Memory**: Keeps track of conversational state while avoiding context bloat.
- **Rule-Based NLP & Sentiment Parsing**: Dynamically determines user intents and sentiment metrics.
- **Production Packaging**: Clean `pyproject.toml` metadata and packaging setup.
- **Complete Test Coverage**: Unit tests utilizing `pytest` to ensure structural integrity.

---

## 📁 Directory Structure

```text
pyproject/
├── src/
│   └── chatbot/
│       ├── __init__.py      # Package initializer
│       ├── main.py          # Interactive CLI main thread
│       ├── bot.py           # Core ChatBot orchestrator
│       ├── config.py        # Environment variable settings configuration
│       ├── database.py      # SQLite logging and context manager
│       ├── memory.py        # Conversational memory buffer
│       ├── nlp.py           # Intent parsing and sentiment analysis
│       └── utils.py         # Text preprocessing helpers
├── tests/
│   ├── __init__.py
│   ├── test_bot.py          # Chatbot flow tests
│   ├── test_memory.py       # Memory buffer tests
│   └── test_nlp.py          # NLP and intent parser tests
├── .gitignore
├── pyproject.toml           # Packaging metadata
├── requirements.txt         # Dev & test requirements
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10 or higher** is recommended.

### Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/nikhiltomar2712/pyproject.git
   cd pyproject
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the package in editable mode along with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

---

## 🎮 Usage

Run the chatbot directly in your terminal:

```bash
chatbot
```

*Alternatively, run the module directly:*
```bash
python3 -m src.chatbot.main
```

### Supported Intents

The bot matches your inputs using text tokenization and answers accordingly:
- **Greetings**: Saying `hello`, `hi`, or `hey` triggers a warm welcome.
- **System Time**: Asking for `time` or `date` outputs the current local time.
- **Weather**: Asking about the `weather` returns a status summary.
- **Help**: Type `help` to list all available commands.
- **Exit**: Type `exit`, `quit`, or `bye` to terminate the session.

---

## 🧪 Testing and Quality Control

### Running Tests

Execute the unit tests using `pytest`:

```bash
pytest
```

### Code Formatting

Format your modifications following standard PEP8 conventions with `black`:

```bash
black src/ tests/
```

---

## 📄 License

This repository is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
