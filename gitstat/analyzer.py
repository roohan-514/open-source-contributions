"""GitHub API repository analysis with caching and rate-limit handling."""

import json
import os
import time
import requests

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "gitstat")
CACHE_TTL = 300  # 5 minutes


class RepoAnalyzer:
    """Fetches and caches GitHub repository analytics."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "gitstat/1.0.0",
        })
        os.makedirs(CACHE_DIR, exist_ok=True)

    def _cache_path(self, owner: str, repo: str) -> str:
        return os.path.join(CACHE_DIR, f"{owner}_{repo}.json")

    def _load_cache(self, owner: str, repo: str) -> dict | None:
        path = self._cache_path(owner, repo)
        if not os.path.isfile(path):
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                cached = json.load(f)
            if time.time() - cached.get("_cached_at", 0) < CACHE_TTL:
                if self.verbose:
                    print("[+] Using cached data")
                return cached
        except (json.JSONDecodeError, KeyError):
            pass
        return None

    def _save_cache(self, owner: str, repo: str, data: dict):
        data["_cached_at"] = time.time()
        path = self._cache_path(owner, repo)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def _request(self, url: str) -> dict | list:
        resp = self.session.get(url)
        if resp.status_code == 403:
            reset = resp.headers.get("X-RateLimit-Reset", "0")
            remaining = resp.headers.get("X-RateLimit-Remaining", "0")
            if remaining == "0":
                wait = max(int(reset) - int(time.time()), 0) + 1
                print(f"[!] Rate limited. Waiting {wait}s...")
                time.sleep(wait)
                return self._request(url)
        if resp.status_code == 404:
            raise ValueError(f"Repository not found: {url}")
        if resp.status_code != 200:
            raise RuntimeError(
                f"GitHub API error {resp.status_code}: {resp.text}"
            )
        return resp.json()

    def analyze(self, owner: str, repo: str) -> dict:
        cached = self._load_cache(owner, repo)
        if cached:
            return cached

        if self.verbose:
            print(f"[+] Fetching repo info for {owner}/{repo}...")

        repo_data = self._request(
            f"https://api.github.com/repos/{owner}/{repo}"
        )

        if self.verbose:
            print("[+] Fetching contributors...")
        contributors = self._request(
            f"https://api.github.com/repos/{owner}/{repo}/contributors?per_page=20"
        )

        if self.verbose:
            print("[+] Fetching languages...")
        languages = self._request(
            f"https://api.github.com/repos/{owner}/{repo}/languages"
        )

        if self.verbose:
            print("[+] Fetching recent commits...")
        commits = self._request(
            f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
        )

        data = {
            "name": repo_data.get("name", repo),
            "full_name": repo_data.get("full_name", f"{owner}/{repo}"),
            "description": repo_data.get("description") or "No description",
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0),
            "open_issues": repo_data.get("open_issues_count", 0),
            "watchers": repo_data.get("subscribers_count", 0),
            "license": (
                repo_data.get("license", {}).get("spdx_id", "N/A")
                if repo_data.get("license")
                else "N/A"
            ),
            "default_branch": repo_data.get("default_branch", "main"),
            "created_at": repo_data.get("created_at", ""),
            "updated_at": repo_data.get("updated_at", ""),
            "pushed_at": repo_data.get("pushed_at", ""),
            "size": repo_data.get("size", 0),
            "topics": repo_data.get("topics", []),
            "homepage": repo_data.get("homepage") or "",
            "language": repo_data.get("language") or "N/A",
            "contributors": [
                {
                    "login": c.get("login", ""),
                    "avatar": c.get("avatar_url", ""),
                    "contributions": c.get("contributions", 0),
                    "profile": c.get("html_url", ""),
                }
                for c in (contributors if isinstance(contributors, list) else [])
            ],
            "total_contributors": (
                len(contributors) if isinstance(contributors, list) else 0
            ),
            "languages": languages if isinstance(languages, dict) else {},
            "recent_commits": [
                {
                    "sha": c.get("sha", "")[:7],
                    "message": (
                        c.get("commit", {}).get("message", "").split("\n")[0]
                    ),
                    "author": (
                        c.get("commit", {}).get("author", {}).get("name", "Unknown")
                    ),
                    "date": c.get("commit", {}).get("author", {}).get("date", ""),
                    "url": c.get("html_url", ""),
                }
                for c in (commits if isinstance(commits, list) else [])
            ],
            "has_issues": repo_data.get("has_issues", False),
            "has_wiki": repo_data.get("has_wiki", False),
            "has_pages": repo_data.get("has_pages", False),
        }

        self._save_cache(owner, repo, data)
        return data
