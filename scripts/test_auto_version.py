"""Exercise version policy and publication against real, temporary Git histories."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import auto_version as versioning


class FakeGitHub:
    repository = "example/website"

    def __init__(self):
        self.prs = {}

    def associated_prs(self, sha):
        return self.prs.get(sha, [])

    def merge(self, sha, number, labels=(), **overrides):
        pr = {"number": number, "title": f"Update {number}",
              "merged_at": "2026-10-21T00:00:00Z", "base": {"ref": "main"},
              "merge_commit_sha": sha, "labels": list(labels)}
        pr.update(overrides)
        self.prs.setdefault(sha, []).append(pr)
        return pr


class VersionPolicyTests(unittest.TestCase):
    def test_semantic_bumps_and_defaults(self):
        self.assertEqual(versioning.label_kind([]), "patch")
        for labels, expected in [(["version:patch"], "patch"),
                                 ([{"name": "version:minor"}], "minor"),
                                 (["docs", "version:major"], "major")]:
            self.assertEqual(versioning.label_kind(labels), expected)
        for kind, expected in [("patch", "2.2.10"), ("minor", "2.3.0"), ("major", "3.0.0")]:
            self.assertEqual(versioning.bump("2.2.9", kind), expected)

    def test_ambiguous_or_unknown_labels_fail(self):
        for labels in [["version:major", "version:minor"], ["version:skip"], ["version:banana"]]:
            with self.assertRaises(ValueError):
                versioning.label_kind(labels)

    def test_invalid_versions_fail(self):
        for value in ["02.2.1", "2.2", "v2.2.1", "2.2.1\nextra", "2.2.1-beta", "2.2.1٢"]:
            with self.assertRaises(ValueError):
                versioning.bump(value, "patch")

    def test_pr_title_is_single_line_and_markdown_escaped(self):
        self.assertEqual(versioning.markdown_title("Fix [link]\n# heading <script>"),
                         r"Fix \[link\] \# heading \<script\>")


class GitHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "work"
        self.root.mkdir()
        self.git("init", "-b", "main")
        self.configure(self.root)
        (self.root / "VERSION").write_text("2.2.1\n")
        (self.root / "CHANGELOG.md").write_text("# Changelog\n\n## Unreleased\n\n### 2.2.1 — Existing\n\n- Keep history.\n")
        self.git("add", ".")
        self.git("commit", "-m", "Baseline")
        anchor = self.git("rev-parse", "HEAD")
        (self.root / ".github").mkdir()
        (self.root / versioning.STATE_PATH).write_text(json.dumps({
            "schema": 1, "version": "2.2.1", "processed_through": anchor, "pull_requests": {},
        }))
        self.git("add", ".")
        self.git("commit", "-m", f"Initialize state\n\n{versioning.TRAILER}")
        self.api = FakeGitHub()

    @staticmethod
    def configure(root):
        versioning.git(root, "config", "user.name", "Version test")
        versioning.git(root, "config", "user.email", "test@example.invalid")

    def git(self, *args):
        return versioning.git(self.root, *args)

    def commit(self, name, content="change", message="Site change", root=None):
        root = root or self.root
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        versioning.git(root, "add", "--", name)
        versioning.git(root, "commit", "-m", message)
        return versioning.git(root, "rev-parse", "HEAD")

    def save_metadata(self):
        self.git("add", "--", *sorted(versioning.METADATA_PATHS))
        self.git("commit", "-m", f"Version metadata\n\n{versioning.TRAILER}")

    def test_merge_order_and_each_pr_gets_a_version(self):
        first = self.commit("one.md")
        second = self.commit("two.md")
        third = self.commit("three.md")
        # API/event order and PR numbers need not match main's integration order.
        self.api.merge(third, 1, ["version:major"])
        self.api.merge(first, 900)
        self.api.merge(second, 50, ["version:minor"])
        self.assertFalse(versioning.ready(self.root))
        result = versioning.reconcile(self.root, self.api)
        self.assertEqual(result, [{"number": 900, "version": "2.2.2"},
                                  {"number": 50, "version": "2.3.0"},
                                  {"number": 1, "version": "3.0.0"}])
        self.save_metadata()
        self.assertTrue(versioning.ready(self.root))
        self.assertEqual(versioning.reconcile(self.root, self.api), [])
        self.assertEqual(self.git("status", "--porcelain"), "")
        changelog = (self.root / "CHANGELOG.md").read_text()
        self.assertLess(changelog.index("### 3.0.0"), changelog.index("### 2.3.0"))
        self.assertIn("- Keep history.", changelog)

    def test_rebase_associations_are_counted_once_at_last_commit(self):
        first = self.commit("one.md")
        last = self.commit("two.md")
        pr = self.api.merge(last, 42)
        self.api.prs[first] = [pr]
        self.assertEqual(versioning.reconcile(self.root, self.api), [{"number": 42, "version": "2.2.2"}])

    def test_merge_commit_counts_one_pr_not_its_feature_commits(self):
        self.git("checkout", "-b", "feature")
        feature_one = self.commit("one.md")
        feature_two = self.commit("two.md")
        self.git("checkout", "main")
        self.git("merge", "--no-ff", "feature", "-m", "Merge feature")
        merged = self.git("rev-parse", "HEAD")
        pr = self.api.merge(merged, 42)
        self.api.prs[feature_one] = self.api.prs[feature_two] = [pr]
        self.assertEqual(versioning.reconcile(self.root, self.api), [{"number": 42, "version": "2.2.2"}])

    def test_closed_unmerged_and_other_branch_prs_consume_no_version(self):
        sha = self.commit("one.md")
        self.api.merge(sha, 1, merged_at=None)
        self.api.merge(sha, 2, base={"ref": "other"})
        self.assertEqual(versioning.reconcile(self.root, self.api), [])
        self.save_metadata()
        self.assertTrue(versioning.ready(self.root))
        self.assertEqual((self.root / "VERSION").read_text(), "2.2.1\n")

    def test_duplicate_pr_association_does_not_increment_again(self):
        first = self.commit("one.md")
        self.api.merge(first, 42)
        versioning.reconcile(self.root, self.api)
        self.save_metadata()
        second = self.commit("two.md")
        self.api.merge(second, 42)
        self.assertEqual(versioning.reconcile(self.root, self.api), [])
        self.assertEqual((self.root / "VERSION").read_text(), "2.2.2\n")

    def test_invalid_label_does_not_partially_write_metadata(self):
        first = self.commit("one.md")
        second = self.commit("two.md")
        self.api.merge(first, 1)
        self.api.merge(second, 2, ["version:major", "version:minor"])
        before = {name: (self.root / name).read_bytes() for name in versioning.METADATA_PATHS}
        with self.assertRaises(ValueError):
            versioning.reconcile(self.root, self.api)
        self.assertEqual(before, {name: (self.root / name).read_bytes() for name in before})

    def test_version_only_human_pr_still_requires_processing(self):
        self.assertTrue(versioning.ready(self.root))
        sha = self.commit("CHANGELOG.md", "# Changelog\n\n## Unreleased\n\nNew note.\n")
        self.assertFalse(versioning.ready(self.root))
        self.api.merge(sha, 42)
        self.assertEqual(versioning.reconcile(self.root, self.api), [{"number": 42, "version": "2.2.2"}])

    def test_bot_trailer_does_not_skip_site_changes(self):
        sha = self.commit("index.md", message=f"Site change\n\n{versioning.TRAILER}")
        self.assertFalse(versioning.metadata_commit(self.root, sha))
        self.assertFalse(versioning.ready(self.root))

    def test_manual_version_mismatch_stops_publication(self):
        (self.root / "VERSION").write_text("2.9.9\n")
        with self.assertRaisesRegex(ValueError, "disagree"):
            versioning.reconcile(self.root, self.api)

    def test_invalid_anchor_stops_the_gate(self):
        path = self.root / versioning.STATE_PATH
        state = json.loads(path.read_text())
        state["processed_through"] = "a" * 40
        path.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError, "first-parent"):
            versioning.ready(self.root)

    def test_build_gate_skips_unprocessed_merge_then_accepts_metadata_commit(self):
        self.commit("one.md")
        sha = self.git("rev-parse", "HEAD")
        self.api.merge(sha, 42)
        output = Path(self.temp.name) / "output"
        script = Path(versioning.__file__).resolve()
        env = dict(os.environ, GITHUB_OUTPUT=str(output))
        subprocess.run([sys.executable, str(script), "gate"], cwd=self.root, env=env,
                       check=True, capture_output=True)
        self.assertEqual(output.read_text(), "ready=false\n")
        versioning.reconcile(self.root, self.api)
        self.save_metadata()
        output.write_text("")
        subprocess.run([sys.executable, str(script), "gate"], cwd=self.root, env=env,
                       check=True, capture_output=True)
        self.assertEqual(output.read_text(), "ready=true\n")

    def test_missing_changelog_marker_fails_before_writing(self):
        self.commit("one.md")
        (self.root / "CHANGELOG.md").write_text("# Notes\n")
        with self.assertRaisesRegex(ValueError, "Unreleased"):
            versioning.reconcile(self.root, self.api)

    def test_push_race_refetches_and_records_both_merges_once(self):
        remote = Path(self.temp.name) / "remote.git"
        subprocess.run(["git", "init", "--bare", "-b", "main", str(remote)], check=True,
                       capture_output=True)
        self.git("remote", "add", "origin", str(remote))
        first = self.commit("one.md")
        self.api.merge(first, 10)
        self.git("push", "-u", "origin", "main")
        concurrent = Path(self.temp.name) / "concurrent"
        subprocess.run(["git", "clone", str(remote), str(concurrent)], check=True, capture_output=True)
        self.configure(concurrent)

        def advance_main(attempt):
            if attempt == 0:
                sha = self.commit("two.md", root=concurrent)
                self.api.merge(sha, 11)
                versioning.git(concurrent, "push", "origin", "main")

        result = versioning.publish(self.root, self.api, before_push=advance_main)
        self.assertEqual(result, [{"number": 10, "version": "2.2.2"},
                                  {"number": 11, "version": "2.2.3"}])
        self.assertEqual(versioning.publish(self.root, self.api), [])
        self.assertTrue(versioning.ready(self.root))
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))
        self.assertTrue((self.root / "two.md").exists())

    def test_rejected_push_does_not_advance_remote_and_can_be_retried(self):
        remote = Path(self.temp.name) / "remote.git"
        subprocess.run(["git", "init", "--bare", "-b", "main", str(remote)], check=True,
                       capture_output=True)
        self.git("remote", "add", "origin", str(remote))
        sha = self.commit("one.md")
        self.api.merge(sha, 42)
        self.git("push", "-u", "origin", "main")
        hook = remote / "hooks/pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        with self.assertRaisesRegex(RuntimeError, "permissions/branch rules"):
            versioning.publish(self.root, self.api)
        self.assertEqual(versioning.git(remote, "rev-parse", "main"), sha)
        self.assertEqual(versioning.git(remote, "show", "main:VERSION"), "2.2.1")
        hook.unlink()
        self.assertEqual(versioning.publish(self.root, self.api), [{"number": 42, "version": "2.2.2"}])
        self.assertEqual(versioning.publish(self.root, self.api), [])


if __name__ == "__main__":
    unittest.main()
