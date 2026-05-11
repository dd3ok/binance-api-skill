#!/usr/bin/env python3
"""Print one Markdown section from an official Binance docs file."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from urllib.parse import urlparse
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ALLOWED_URLS = (
    ("raw.githubusercontent.com", "/binance/binance-spot-api-docs/"),
    ("github.com", "/binance/binance-spot-api-docs/"),
    ("developers.binance.com", "/docs/binance-spot-api-docs/"),
)


def normalize(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def read_text(source: str) -> str:
    if source.startswith(("http://", "https://")):
        parsed = urlparse(source)
        if parsed.scheme != "https":
            raise ValueError("only https URLs are allowed")
        if not any(parsed.netloc == host and parsed.path.startswith(path) for host, path in ALLOWED_URLS):
            raise ValueError("URL must point to official Binance Spot API docs")
        with urllib.request.urlopen(source, timeout=20) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset)
    return Path(source).read_text(encoding="utf-8")


def extract_section(markdown: str, heading: str) -> str:
    wanted = normalize(heading)
    lines = markdown.splitlines()
    start = None
    level = None

    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if not match:
            continue
        title = normalize(match.group(2))
        if title == wanted:
            start = index
            level = len(match.group(1))
            break

    if start is None or level is None:
        raise ValueError(f"heading not found: {heading}")

    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = HEADING_RE.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break

    section = lines[start:end]
    while section and not section[-1].strip():
        section.pop()
    while section and re.fullmatch(r"\s*<a\s+id=\"[^\"]+\"></a>\s*", section[-1]):
        section.pop()
    while section and not section[-1].strip():
        section.pop()
    return "\n".join(section).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", "--source", dest="source", required=True, help="Raw GitHub URL or local Markdown path")
    parser.add_argument("--heading", required=True, help="Exact Markdown heading text without leading #")
    args = parser.parse_args()

    try:
        print(extract_section(read_text(args.source), args.heading), end="")
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
