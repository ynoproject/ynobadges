#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable, Set, List

JSON_ROOT = Path("./badges")
JSON_GLOB = "**/*.json"
ARTIST_KEY = "art"
MD_PATH = Path("info/CREDITS.md")

START_MARKER = "<!-- CREDITS:START -->"
END_MARKER = "<!-- CREDITS:END -->"

ONLY_CHANGED_JSON = os.environ.get("ONLY_CHANGED_JSON", "1") == "1"


def git_changed_files() -> List[Path]:
    """
    list all changed JSON files in the last commit.
    """
    cmd = ["git", "diff", "--name-only", "HEAD~1..HEAD"]
    out = subprocess.check_output(cmd, text=True).splitlines()
    return [Path(p.strip()) for p in out if p.strip()]


def iter_json_files() -> Iterable[Path]:
    """
    Iterate over all JSON files in the badges directory.
    """
    if not ONLY_CHANGED_JSON:
        yield from JSON_ROOT.glob(JSON_GLOB)

    for p in git_changed_files():
        if p.suffix.lower() == ".json" and p.exists():
            try:
                if "badges" in p.parts:
                    badges_idx = p.parts.index("badges")
                    if badges_idx < len(p.parts) - 1:
                        yield p
            except (ValueError, IndexError):
                continue


def extract_names_from_value(v) -> Set[str]:
    """
    extract artist names from a value.
    """
    names: Set[str] = set()

    if v is None:
        return names

    if not isinstance(v, str):
        raise ValueError(f"Expected a string, got {type(v)}")

    s = v.strip()
    if not s:
        return names

    # co-authorship
    parts = s.split(" & ")
    for part in parts:
        part = part.strip()
        if not part:
            continue

        if "," in part:
            for name in part.split(","):
                name = name.strip()
                if name:
                    names.add(name)
        else:
            names.add(part)

    return names


def find_author_names(obj) -> Set[str]:
    """
    recursively find artist names from a JSON object.
    """
    names: Set[str] = set()

    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and k == ARTIST_KEY:
                names |= extract_names_from_value(v)
            names |= find_author_names(v)

    elif isinstance(obj, list):
        for item in obj:
            names |= find_author_names(item)

    return names


def read_json(path: Path):
    """
    read a JSON file and return a dictionary.
    """
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return None


def build_credits_block(names: List[str]) -> str:
    """
    build a credits block from a list of artist names.
    """
    if not names:
        return "*(No credits found yet.)"

    lines = []
    for n in names:
        lines.append(f"* {n}")
    return "\n".join(lines)


def extract_existing_names(text: str, start: str, end: str) -> Set[str]:
    """
    extract existing artist names from a CREDITS.md file.
    """
    pattern = re.compile(
        re.escape(start) + r"(.*?)" + re.escape(end),
        flags=re.DOTALL
    )

    match = pattern.search(text)
    if not match:
        return set()

    block_content = match.group(1)
    names: Set[str] = set()

    for line in block_content.splitlines():
        line = line.strip()
        if line.startswith("* "):
            name = line[2:].strip()  # remove "* "
            if name:
                names.add(name)

    return names


def replace_block(text: str, start: str, end: str, new_block: str) -> str:
    """
    replace the block between start and end with new_block.
    """
    pattern = re.compile(
        re.escape(start) + r"(.*?)" + re.escape(end),
        flags=re.DOTALL
    )

    if not pattern.search(text):
        raise RuntimeError(f"Markers not found in {MD_PATH}: {start} / {end}")

    replacement = start + "\n" + new_block.rstrip() + "\n" + end
    return pattern.sub(replacement, text, count=1)


def main() -> int:
    # read the existing CREDITS.md file and extract existing artist names
    readme = MD_PATH.read_text(encoding="utf-8")
    existing_names = extract_existing_names(readme, START_MARKER, END_MARKER)

    new_names: Set[str] = set()

    for path in iter_json_files():
        obj = read_json(path)
        if obj is None:
            continue
        found = find_author_names(obj)
        for n in found:
            new_names.add(n)

    all_names = existing_names | new_names

    def _sort_key(name: str) -> tuple:
        name_lower = name.lower().strip()
        if name_lower.isdigit():
            return (0, int(name_lower))
        return (1, name_lower)

    sorted_names = sorted(all_names, key=_sort_key)
    block = build_credits_block(sorted_names)
    updated = replace_block(readme, START_MARKER, END_MARKER, block)

    if updated != readme:
        MD_PATH.write_text(updated, encoding="utf-8")
        print(f"Updated {MD_PATH} with {len(sorted_names)} credit(s).")
    else:
        print("No changes to CREDITS.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
