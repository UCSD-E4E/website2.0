"""Assign one website version per merged PR, in main's first-parent order.

Only the opt-in Actions workflow calls publish. Tests use temporary repositories;
no credentials, third-party packages, or PR-controlled shell expressions are needed.
"""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys


STATE_PATH = ".github/versioning-state.json"
METADATA_PATHS = {"VERSION", "CHANGELOG.md", STATE_PATH}
TRAILER = "Website-Version-Update: true"
VERSION_RE = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)")


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def bump(version, kind):
    if not VERSION_RE.fullmatch(version):
        raise ValueError("VERSION must be MAJOR.MINOR.PATCH without leading zeroes")
    major, minor, patch = map(int, version.split("."))
    if kind == "major":
        return f"{major + 1}.0.0"
    if kind == "minor":
        return f"{major}.{minor + 1}.0"
    if kind == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"Unknown version change: {kind}")


def label_kind(labels):
    labels = {label["name"] if isinstance(label, dict) else label for label in labels}
    version_labels = {label for label in labels if label.startswith("version:")}
    if version_labels - {"version:patch", "version:minor", "version:major"}:
        raise ValueError("Use version:patch, version:minor, or version:major")
    if len(version_labels) > 1:
        raise ValueError("A PR may have only one version:* label")
    return next(iter(version_labels), "version:patch").split(":")[1]


def load_state(root):
    state = json.loads((root / STATE_PATH).read_text())
    if state.get("schema") != 1:
        raise ValueError("Unsupported website version state schema")
    version = (root / "VERSION").read_text().strip()
    if not VERSION_RE.fullmatch(version) or version != state.get("version"):
        raise ValueError("VERSION and versioning-state.json disagree; do not bump VERSION manually")
    anchor = state.get("processed_through", "")
    if not re.fullmatch(r"[0-9a-f]{40}", anchor):
        raise ValueError("Invalid processed_through commit")
    history = git(root, "rev-list", "--first-parent", "HEAD").splitlines()
    if anchor not in history:
        raise ValueError("Version state anchor is not on main's first-parent history")
    if not isinstance(state.get("pull_requests"), dict):
        raise ValueError("Missing processed PR ledger")
    return state


def metadata_commit(root, sha):
    """Only our marked, metadata-only follow-up commits can bypass versioning."""
    message = git(root, "show", "-s", "--format=%B", sha).splitlines()
    paths = set(git(root, "diff", "--name-only", f"{sha}^", sha).splitlines())
    return TRAILER in message and STATE_PATH in paths and paths <= METADATA_PATHS


def pending_commits(root, state):
    commits = git(root, "rev-list", "--reverse", "--first-parent",
                  f"{state['processed_through']}..HEAD").splitlines()
    return [sha for sha in commits if not metadata_commit(root, sha)]


def ready(root):
    state = load_state(root)
    return not pending_commits(root, state)


class GitHub:
    def __init__(self, repository):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ValueError("Invalid GitHub repository")
        self.repository = repository

    def associated_prs(self, sha):
        # --slurp preserves pagination as valid JSON instead of concatenated arrays.
        pages = json.loads(subprocess.check_output([
            "gh", "api", "--paginate", "--slurp",
            f"repos/{self.repository}/commits/{sha}/pulls?per_page=100",
        ], text=True))
        return [pr for page in pages for pr in page]


def markdown_title(title):
    title = " ".join(title.split())
    return re.sub(r"([\\`*_{}\[\]<>()#!|])", r"\\\1", title)


def reconcile(root, api, branch="main"):
    """Prepare metadata in memory first, so an invalid PR cannot cause half a bump."""
    state = load_state(root)
    commits = pending_commits(root, state)
    if not commits:
        return []
    changelog = (root / "CHANGELOG.md").read_text()
    marker = "## Unreleased\n"
    if changelog.count(marker) != 1:
        raise ValueError("CHANGELOG.md must have exactly one Unreleased section")
    processed = []
    for sha in commits:
        for pr in sorted(api.associated_prs(sha), key=lambda item: item["number"]):
            # Rebased PRs can appear on several commits; count only their final
            # integration commit. Ignore PR associations from other target branches.
            if (not pr.get("merged_at") or pr["base"]["ref"] != branch
                    or pr["merge_commit_sha"] != sha):
                continue
            number = str(pr["number"])
            if number in state["pull_requests"]:
                continue
            kind = label_kind(pr.get("labels", []))
            version = bump(state["version"], kind)
            state["version"] = version
            state["pull_requests"][number] = {
                "version": version, "bump": kind, "merge_commit": sha,
            }
            title = markdown_title(pr["title"])
            section = (f"\n### {version} — PR #{number}\n\n"
                       f"- {title} ([#{number}](https://github.com/{api.repository}/pull/{number})).\n")
            changelog = changelog.replace(marker, marker + section, 1)
            processed.append({"number": int(number), "version": version})
    # Direct pushes consume no PR version, but must be recorded before publishing.
    state["processed_through"] = git(root, "rev-parse", "HEAD")
    (root / "VERSION").write_text(state["version"] + "\n")
    (root / "CHANGELOG.md").write_text(changelog)
    (root / STATE_PATH).write_text(json.dumps(state, indent=2) + "\n")
    return processed


def publish(root, api, branch="main", attempts=5, before_push=None):
    """Run only in a disposable CI checkout; never force-push or overwrite main."""
    if git(root, "status", "--porcelain"):
        raise ValueError("Version publisher requires a clean, disposable checkout")
    for attempt in range(attempts):
        git(root, "fetch", "origin", branch)
        # Discard only a previous failed attempt inside this dedicated CI checkout.
        git(root, "checkout", "--detach", "--force", f"origin/{branch}")
        processed = reconcile(root, api, branch)
        if not git(root, "status", "--porcelain"):
            return []
        git(root, "add", "--", *sorted(METADATA_PATHS))
        git(root, "commit", "-m", f"chore(version): record merged PR versions\n\n{TRAILER}")
        if before_push:
            before_push(attempt)
        result = subprocess.run(["git", "-C", str(root), "push", "origin", f"HEAD:{branch}"],
                                text=True, capture_output=True)
        if result.returncode == 0:
            return processed
        # Retry only a non-fast-forward race. Permission/branch-rule failures stop.
        remote = git(root, "ls-remote", "origin", f"refs/heads/{branch}").split()[0]
        parent = git(root, "rev-parse", "HEAD^")
        if remote == parent or attempt == attempts - 1:
            raise RuntimeError("Version commit could not be pushed. Check App permissions/branch rules.\n"
                               + result.stderr)
    raise RuntimeError("main kept advancing; rerun the version workflow")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["publish", "verify", "gate", "validate-labels"])
    args = parser.parse_args()
    root = Path.cwd()
    if args.command == "validate-labels":
        event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
        print(label_kind(event["pull_request"].get("labels", [])))
    elif args.command in ("verify", "gate"):
        is_ready = ready(root)
        if args.command == "gate":
            with open(os.environ["GITHUB_OUTPUT"], "a") as output:
                output.write(f"ready={str(is_ready).lower()}\n")
            print("Version metadata is current" if is_ready else
                  "Waiting for Automatic website version to record this merge")
        elif not is_ready:
            raise ValueError("This commit has not been processed by automatic website versioning")
    else:
        api = GitHub(os.environ["GITHUB_REPOSITORY"])
        print(json.dumps(publish(root, api)))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
