# Contributing Guidelines

Thank you for your interest in contributing to the **AI Chatbot** (`pyproject`) repository! We welcome bug reports, feature suggestions, and pull requests.

## 🛠️ Local Development Setup

To set up a local development environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nikhiltomar2712/pyproject.git
   cd pyproject
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install development requirements:
   ```bash
   pip install -e ".[dev]"
   ```

## 🧪 Testing Your Changes

Before submitting your changes, please run the unit tests to ensure that everything is working as expected:

```bash
pytest
```

Make sure to format your code using `black` to adhere to formatting standards:

```bash
black src/ tests/
```

## 📬 Submitting a Pull Request

1. Fork the repository and create your branch from `main`.
2. Commit your changes with clear, descriptive commit messages.
3. Push to your fork and submit a pull request (PR).
4. Ensure all CI workflows and unit tests pass on your PR.
