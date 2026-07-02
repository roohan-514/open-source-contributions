"""HTML and Markdown report generation for gitstat."""

import os
from datetime import datetime


class ReportGenerator:
    """Generates formatted reports from repo analysis data."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def _load_template(self) -> str:
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        template_path = os.path.join(template_dir, "report.html")
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()

    def generate_html(self, data: dict, repo_url: str) -> str:
        if self.verbose:
            print("[+] Generating HTML report...")

        template = self._load_template()

        lang_total = sum(data["languages"].values()) or 1
        lang_bars = ""
        lang_labels = ""
        colors = [
            "#e06c75", "#61afef", "#98c379", "#d19a66", "#56b6c2",
            "#c678dd", "#abb2bf", "#be5046", "#7ec8e3", "#e5c07b",
        ]
        for i, (lang, bytes_) in enumerate(sorted(
            data["languages"].items(), key=lambda x: -x[1]
        )):
            pct = (bytes_ / lang_total) * 100
            color = colors[i % len(colors)]
            lang_bars += (
                f'<div class="lang-bar">'
                f'<span class="lang-name">{lang}</span>'
                f'<div class="lang-bar-track">'
                f'<div class="lang-bar-fill" style="width:{pct:.1f}%;background:{color}"></div>'
                f'</div>'
                f'<span class="lang-pct">{pct:.1f}%</span>'
                f'</div>\n'
            )
            lang_labels += (
                f'<span class="lang-label">'
                f'<span class="lang-dot" style="background:{color}"></span>{lang}'
                f'</span>\n'
            )

        contrib_rows = ""
        for i, c in enumerate(data["contributors"], 1):
            contrib_rows += (
                f'<tr>'
                f'<td>{i}</td>'
                f'<td><img class="avatar" src="{c["avatar"]}&s=32" alt=""> '
                f'<a href="{c["profile"]}">{c["login"]}</a></td>'
                f'<td>{c["contributions"]}</td>'
                f'</tr>\n'
            )

        commit_rows = ""
        for c in data["recent_commits"]:
            commit_rows += (
                f'<tr>'
                f'<td><code>{c["sha"]}</code></td>'
                f'<td>{c["author"]}</td>'
                f'<td>{c["message"]}</td>'
                f'<td>{c["date"][:10]}</td>'
                f'</tr>\n'
            )

        topics_html = ""
        for t in data["topics"]:
            topics_html += f'<span class="topic-tag">{t}</span>\n'

        replacements = {
            "{{REPO_NAME}}": data["name"],
            "{{FULL_NAME}}": data["full_name"],
            "{{DESCRIPTION}}": data["description"],
            "{{REPO_URL}}": repo_url,
            "{{STARS}}": str(data["stars"]),
            "{{FORKS}}": str(data["forks"]),
            "{{OPEN_ISSUES}}": str(data["open_issues"]),
            "{{WATCHERS}}": str(data["watchers"]),
            "{{LICENSE}}": data["license"],
            "{{DEFAULT_BRANCH}}": data["default_branch"],
            "{{LANGUAGE}}": data["language"],
            "{{SIZE_KB}}": f"{data['size']:.0f}",
            "{{CREATED_AT}}": data["created_at"][:10] if data["created_at"] else "N/A",
            "{{UPDATED_AT}}": data["updated_at"][:10] if data["updated_at"] else "N/A",
            "{{PUSHED_AT}}": data["pushed_at"][:10] if data["pushed_at"] else "N/A",
            "{{TOTAL_CONTRIBUTORS}}": str(data["total_contributors"]),
            "{{TOTAL_COMMITS_SHOWN}}": str(len(data["recent_commits"])),
            "{{LANG_BARS}}": lang_bars,
            "{{LANG_LABELS}}": lang_labels,
            "{{CONTRIB_ROWS}}": contrib_rows,
            "{{COMMIT_ROWS}}": commit_rows,
            "{{TOPICS}}": topics_html,
            "{{GENERATED_AT}}": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        }

        for key, val in replacements.items():
            template = template.replace(key, val)

        return template

    def generate_markdown(self, data: dict, repo_url: str) -> str:
        lines = [
            f"# {data['full_name']} — Repository Report",
            "",
            f"**Description:** {data['description']}",
            "",
            "## Overview",
            "",
            f"- **Stars:** {data['stars']}",
            f"- **Forks:** {data['forks']}",
            f"- **Open Issues:** {data['open_issues']}",
            f"- **Watchers:** {data['watchers']}",
            f"- **License:** {data['license']}",
            f"- **Language:** {data['language']}",
            f"- **Default Branch:** {data['default_branch']}",
            "",
            "## Languages",
            "",
        ]
        lang_total = sum(data["languages"].values()) or 1
        for lang, bytes_ in sorted(
            data["languages"].items(), key=lambda x: -x[1]
        ):
            pct = (bytes_ / lang_total) * 100
            lines.append(f"- {lang}: {pct:.1f}%")

        lines += [
            "",
            "## Top Contributors",
            "",
            "| # | Contributor | Contributions |",
            "|---|-------------|--------------|",
        ]
        for i, c in enumerate(data["contributors"], 1):
            lines.append(f"| {i} | {c['login']} | {c['contributions']} |")

        lines += [
            "",
            "## Recent Commits",
            "",
            "| SHA | Author | Message | Date |",
            "|-----|--------|---------|------|",
        ]
        for c in data["recent_commits"]:
            lines.append(
                f"| {c['sha']} | {c['author']} | {c['message']} | {c['date'][:10]} |"
            )

        lines += [
            "",
            "---",
            f"*Report generated by gitstat on {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*",
            "",
        ]
        return "\n".join(lines)
