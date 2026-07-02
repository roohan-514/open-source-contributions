# 🌍 Open Source Contributions

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-open--source--contributions-181717?logo=github)](https://github.com/roohan-514/open-source-contributions)
[![CLI Tool](https://img.shields.io/badge/Tool-gitstat-58a6ff)](#-gitstat)

> A practical demonstration of open source contribution skills — featuring **gitstat**, a CLI tool that generates beautiful GitHub repository analytics reports.

---

## 📦 What's Inside

This repository serves as both a **portfolio** of OSS contribution practices and a **usable tool** for the community.

| Component | Description |
|-----------|-------------|
| `gitstat/` | Python CLI tool — analyze any public GitHub repo and get a rich HTML report |
| `CONTRIBUTING.md` | Well-structured contribution guidelines for this project |
| `CODE_OF_CONDUCT.md` | Standard Contributor Covenant |
| `LICENSE` | MIT License |
| `setup.py` | PyPI-ready package configuration |

---

## 🛠️ gitstat

**gitstat** is a command-line tool that takes a GitHub repository URL and generates a comprehensive, beautifully styled HTML report with:

- ⭐ Stars, forks, open issues, watchers
- 🧑‍💻 Top contributors with avatar and commit counts
- 📝 Recent commits (SHA, author, message, date)
- 📊 Language breakdown with visual bars
- 📋 Repository metadata (license, branch, dates, size)
- 🏷️ Repository topics
- 🚀 Rate-limit aware GitHub API calls with caching

### Installation

```bash
# Via pip (once published)
pip install gitstat

# Or install from source
git clone https://github.com/roohan-514/open-source-contributions.git
cd open-source-contributions
pip install -e .
```

### Usage

```bash
# Basic usage
gitstat https://github.com/roohan-514/rag-chatbot-system

# Specify output file
gitstat https://github.com/roohan-514/rag-chatbot-system -o my-report.html

# Verbose mode (see API calls)
gitstat https://github.com/roohan-514/rag-chatbot-system --verbose

# Markdown format
gitstat https://github.com/roohan-514/rag-chatbot-system -f markdown
```

---

## 🌱 My OSS Journey

Open source software is the backbone of the modern internet. My journey began by using open source tools, then fixing small issues, and eventually building and sharing tools of my own.

**Why I contribute:**
- **Learn from the best** — reading high-quality code sharpens my skills
- **Give back** — OSS tools power my projects every day
- **Build reputation** — a public GitHub footprint demonstrates real ability
- **Collaborate globally** — work with developers from every time zone

**Projects I've contributed to:**
- [rag-chatbot-system](https://github.com/roohan-514/rag-chatbot-system) — RAG-based document Q&A with LangChain
- This repository — building and documenting OSS best practices

---

## ❤️ Why Contribute to OSS?

| Reason | Impact |
|--------|--------|
| **Skill growth** | Read, write, and review production-grade code |
| **Portfolio** | Tangible proof of your abilities for employers |
| **Community** | Join a global network of passionate developers |
| **Impact** | Your code helps thousands (or millions!) of users |
| **Reciprocity** | The software you love exists because others contributed |

---

## ⚖️ License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 📬 Get in Touch

- GitHub: [@roohan-514](https://github.com/roohan-514)
- Email: roohan.rizvi@gmail.com

*Built with ❤️ for the open source community.*
