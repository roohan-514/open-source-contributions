"""Argument parsing and CLI entry point for gitstat."""

import argparse
import sys
from urllib.parse import urlparse

from gitstat.analyzer import RepoAnalyzer
from gitstat.report_generator import ReportGenerator


def parse_repo_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    parts = path.split("/")
    if len(parts) < 2 or not all(parts[:2]):
        raise ValueError(
            "Invalid GitHub repo URL. Expected format: "
            "https://github.com/owner/repo"
        )
    return parts[0], parts[1].replace(".git", "")


def main():
    parser = argparse.ArgumentParser(
        prog="gitstat",
        description="Generate beautiful GitHub repo analytics reports.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  gitstat https://github.com/roohan-514/rag-chatbot-system\n"
            "  gitstat https://github.com/roohan-514/rag-chatbot-system -o report.html -f html\n"
            "  gitstat https://github.com/roohan-514/rag-chatbot-system --verbose\n"
        ),
    )
    parser.add_argument(
        "repo_url",
        type=str,
        help="Full GitHub repository URL (e.g. https://github.com/owner/repo)",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="",
        help="Output file path (default: <repo>-report.html)",
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        choices=["html", "markdown"],
        default="html",
        help="Output format (default: html)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    try:
        owner, repo = parse_repo_url(args.repo_url)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"[+] Parsed repo: {owner}/{repo}")
        print(f"[+] Fetching data from GitHub API...")

    analyzer = RepoAnalyzer(verbose=args.verbose)
    try:
        data = analyzer.analyze(owner, repo)
    except Exception as e:
        print(f"Error analyzing repository: {e}", file=sys.stderr)
        sys.exit(1)

    if not args.output:
        args.output = f"{repo}-report.html"

    generator = ReportGenerator(verbose=args.verbose)

    if args.format == "html":
        output = generator.generate_html(data, args.repo_url)
    else:
        output = generator.generate_markdown(data, args.repo_url)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Report generated: {args.output}")

    if args.verbose:
        print(f"[+] Done. Report saved to {args.output}")


if __name__ == "__main__":
    main()
