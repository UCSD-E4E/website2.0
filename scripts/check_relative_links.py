"""Reject document-relative hyperlinks in generated HTML (no dependencies)."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class LinkChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"a", "area"}:
            return
        href = dict(attrs).get("href")
        if href is None:
            return
        href = href.strip()
        if not href or href.startswith(("/", "#", "?")):
            return
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", href):
            return
        self.errors.append((self.getpos()[0], href))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    files = sorted(args.directory.rglob("*.html"))
    if not files:
        parser.error(f"No HTML files found in {args.directory}; build the site first.")
    failures = 0
    for path in files:
        checker = LinkChecker()
        checker.feed(path.read_text(encoding="utf-8"))
        checker.close()
        for line, href in checker.errors:
            print(f"{path}:{line}: document-relative hyperlink {href!r}; use a root-relative or absolute URL", file=sys.stderr)
            failures += 1
    if failures:
        print(f"Found {failures} document-relative hyperlinks.", file=sys.stderr)
        return 1
    print(f"Checked {len(files)} HTML files: no document-relative hyperlinks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
