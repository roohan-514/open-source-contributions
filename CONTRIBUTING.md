# Contributing to Open Source Contributions

First off, thank you for considering contributing! 🎉

Following these guidelines helps us maintain a healthy, welcoming open source project.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs

1. **Use the GitHub issue tracker** — search existing issues first to avoid duplicates.
2. **Provide a clear title and description** — include steps to reproduce, expected vs actual behavior, and your environment (OS, Python version).

### Suggesting Features

1. Open a feature request issue describing what you'd like to see and why.
2. Be specific about the use case. If possible, include examples of how the feature would work.

### Pull Requests

1. **Fork the repository** and create a branch from `main`.
2. **Run existing tests** before making changes.
   ```bash
   python -m pytest tests/
   ```
3. **Write or update tests** for any new functionality.
4. **Keep changes focused** — one pull request per feature or fix.
5. **Write clear commit messages** following conventional commits:
   - `feat: add --json output format`
   - `fix: handle rate limit correctly`
   - `docs: update README with examples`
6. **Update documentation** if you change behavior.
7. **Ensure the CI passes** — lint, type-check, and tests must all pass.

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/open-source-contributions.git
cd open-source-contributions

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in editable mode
pip install -e .
```

### Code Style

- Follow **PEP 8**.
- Use **type hints** wherever practical.
- Keep functions small and focused.
- Prefer readability over cleverness.
- Use `snake_case` for functions/variables, `PascalCase` for classes.

## Questions?

Open a discussion in the GitHub Issues tab with the "question" label, or reach out to roohan.rizvi@gmail.com.

Thank you for helping make open source better! ❤️
