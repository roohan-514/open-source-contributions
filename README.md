<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/CLI-gitstat-58a6ff?style=for-the-badge" alt="gitstat"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT"/>
  <img src="https://img.shields.io/github/stars/roohan-514/open-source-contributions?style=for-the-badge" alt="Stars"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome"/>
</p>

<h1 align="center">Open Source Contributions</h1>

<p align="center">
  <em>A CLI tool and OSS portfolio — featuring <b>gitstat</b>, a utility that turns any GitHub repo into a beautiful analytics report.</em>
</p>

---

## gitstat

**gitstat** is a zero-dependency Python CLI that takes a GitHub repo URL and generates a comprehensive HTML (or Markdown) analytics report. No API token required for public repos.

### Features

- Stars, forks, open issues, watchers at a glance
- Top contributors with avatars and commit counts
- Recent commits with SHA, author, message, and date
- Language breakdown with visual bars
- Repo metadata: license, branch, dates, size
- Rate-limit aware API calls with caching
- HTML reports with clean, responsive design
- Markdown reports for embedding in docs

### Quick Start

```bash
pip install gitstat

# Or from source
git clone https://github.com/roohan-514/open-source-contributions.git
cd open-source-contributions
pip install -e .
```

### Usage

```bash
# Basic
gitstat https://github.com/roohan-514/rag-chatbot-system

# Custom output
gitstat https://github.com/roohan-514/rag-chatbot-system -o report.html

# Markdown format
gitstat https://github.com/roohan-514/rag-chatbot-system -f markdown

# Verbose mode
gitstat https://github.com/roohan-514/rag-chatbot-system --verbose
```

### Sample Output

The HTML report includes:
- Repository overview with stats cards
- Top contributors section with profile links
- Commit history table
- Language distribution bar chart (pure CSS)
- Full metadata footer

---

## Why This Repo Exists

I built **gitstat** to scratch my own itch — I wanted a quick way to generate shareable repo analytics without opening the GitHub UI. Then I turned it into a showcase of OSS contribution practices.

| Resource | What it covers |
|----------|---------------|
| `gitstat/` | The CLI tool — installable, documented, tested |
| `CONTRIBUTING.md` | Real contribution guide for this project |
| `CODE_OF_CONDUCT.md` | Standard Contributor Covenant |
| `setup.py` | PyPI-ready packaging |

---

## Contributing

Bug reports, feature requests, and PRs are welcome. Check [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## License

MIT
