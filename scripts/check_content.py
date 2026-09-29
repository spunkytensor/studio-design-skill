"""Validate the reviewed content-only profile without third-party dependencies."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


SKILL = "skills/designing-translucent-interfaces"
CONTENT = {"README.md", "UNLICENSE", f"{SKILL}/SKILL.md", f"{SKILL}/UNLICENSE"}
POLICY = {
    ".github/CODEOWNERS", ".github/dependabot.yml",
    ".github/workflows/public-repo-security.yml", "SECURITY.md", "CONTRIBUTING.md",
    "THIRD_PARTY_NOTICES.txt", "docs/baseline-adoption.md", "content-inventory.json",
    "scripts/check_content.py", "tests/test_content.py",
}


def check(root, tracked):
    expected = CONTENT | POLICY
    if set(tracked) != expected:
        raise ValueError(f"Content-only profile needs review: extra={sorted(set(tracked) - expected)}, missing={sorted(expected - set(tracked))}")
    for name in tracked:
        path = root / name
        if path.is_symlink() or not path.is_file() or path.resolve() != path.absolute():
            raise ValueError(f"Not a regular in-tree file: {name}")

    inventory = json.loads((root / "content-inventory.json").read_text())
    if inventory["profile"] != "content-only" or set(inventory["files"]) != CONTENT:
        raise ValueError("Inventory must cover exactly the distributed content")
    for name, entry in inventory["files"].items():
        if entry["license"] != "Unlicense" or not entry["origin"].strip():
            raise ValueError(f"Missing license/provenance: {name}")
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Content changed; review provenance and update inventory: {name}")
    if (root / "UNLICENSE").read_bytes() != (root / SKILL / "UNLICENSE").read_bytes():
        raise ValueError("Bundled Unlicense differs from root")

    skill = (root / SKILL / "SKILL.md").read_text()
    if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
        raise ValueError("Missing skill frontmatter")
    frontmatter = skill.split("---\n", 2)[1]
    if not all(re.search(pattern, frontmatter, re.MULTILINE) for pattern in (
        r"^name: designing-translucent-interfaces$", r"^license: Unlicense$",
        r'^description: "[^"\n]+"$',
    )):
        raise ValueError("Skill identity/license/description contract changed")

    for name in sorted(tracked):
        if not name.endswith(".md"):
            continue
        for target in re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", (root / name).read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (root / name).parent / unquote(url.path)
            if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
                raise ValueError(f"Broken or escaping local link in {name}: {target}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().strip("\0").split("\0")
    try:
        check(root, tracked)
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {len(tracked)} tracked files; 4 distributed hashes; licenses, skill identity and local links")
    print("Dependency/CVE scan and package SBOM: not applicable (content-only)")
