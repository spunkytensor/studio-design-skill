# Contributing

Open an issue or pull request describing the intended change. Keep the skill
product-neutral and preserve its existing discovery layout, frontmatter identity,
and bundled Unlicense. Changes to design guidance must follow the skill's own
verification requirements; documentation checks do not verify rendered UI.

Run these checks from the repository root with Python 3.12 or newer:

```sh
python3 scripts/check_content.py
python3 -m unittest discover -s tests -v
```

The inventory covers distributed material, not installed dependencies. For changes
to its files, review authorship, upstream sources, licenses and required notices,
then update the SHA-256 in `content-inventory.json`. Do not merely refresh hashes
to silence a failure. Preserve third-party copyright, license and NOTICE texts;
record unknown provenance and resolve it before distributing new material.
The repository's Unlicense does not override third-party terms. Include any
required notices inside the installed skill as well as the source archive.

New tracked files require explicit review of the content-only profile and its
allowlist. If adding executable products, dependencies, vendored code, fonts,
images, models or build outputs, reassess inventory and scanning before merging.
See [the adoption record](docs/baseline-adoption.md) for the pinned shared scanner
and release requirements. The Python checks use only the standard library; do not
add test dependencies without updating that assessment.

Never commit credentials or sensitive reports. Follow [SECURITY.md](SECURITY.md).
Workflow and policy changes require maintainer review. Contributions retain the
existing [Unlicense](UNLICENSE); do not submit material you cannot license or
redistribute on the stated terms.
