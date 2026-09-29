# Content-only baseline adoption

- Maintainer: Spunky Tensor (`@spunkytensor`).
- Supported line: current `main`; no published releases or tags at review time.
- Reviewed on: 2026-09-29.
- Shared baseline: [ed53814ed23f76c11fa4a91f57f99de903c18bfc](https://github.com/spunkytensor/.github/tree/ed53814ed23f76c11fa4a91f57f99de903c18bfc), including README, baseline, onboarding and Trivy workflow.
- Profile: **content-only**, with standard-library Python validation tooling.

## Distribution and inventory

Users obtain a Git source archive/checkout or install the
`skills/designing-translucent-interfaces/` directory. The canonical skill source
and both Unlicense texts remain unchanged. `content-inventory.json` identifies
the four original distributed files by SHA-256, origin and declared license.
Policy and CI tooling are explicitly allowlisted by the validator. GitHub-hosted
Actions and the runner's Python are CI tools, not components of the installed skill.

The [attribution review](../THIRD_PARTY_NOTICES.txt) distinguishes repository
provenance from proof of authorship. The installed directory currently needs only
its bundled Unlicense; if third-party material is added, required notices must
travel inside that directory as well as in repository and release archives.

## Automated coverage

**Spunky Tensor security / Content-only checks** runs on pull requests, `main`
pushes, manual dispatch and nightly at **09:59 UTC** (01:59 PST / 02:59 PDT).
It checks exact tracked-file coverage (new files require profile review), regular
files rather than symlinks/submodules, distributed-file hashes and provenance
metadata, identical licenses, skill frontmatter identity, and the existence of
inline relative Markdown link targets. It does not fetch external links or
validate fragment anchors. Regression tests exercise failing inputs. Actions are
SHA-pinned, use a read-only token and do not persist checkout credentials.
Dependabot checks GitHub Actions weekly.

There are no resolved source/build/runtime dependencies, containers, native
libraries, vendored assets or model weights to scan. **Dependency review, package
CVE scanning and package SBOM generation are not applicable to this profile.**
The shared Trivy workflow correctly rejects empty inventories; it is deliberately
not invoked, and no fake passing SBOM or clean-CVE claim is produced. The content
inventory is not an SPDX/CycloneDX SBOM or a legal certification. No prior security
scanner existed to remove. CodeQL is not configured for this documentation product;
the small standard-library validator is tested, not CodeQL-analyzed.

If dependencies or executable artifacts are introduced, adopt
`spunkytensor/.github/.github/workflows/trivy.yml@ed53814ed23f76c11fa4a91f57f99de903c18bfc`
with `baseline-sha` set to that same full SHA,
with nightly `59 9 * * *`, PR and default-branch events. Reconcile actual
distributed inventories, test vulnerable and scanner-failure cases, retain High
and Critical gates including unfixed findings, and publish SPDX/CycloneDX evidence
for applicable releases. Actions updates do not replace review of a pinned Trivy
version. The separately downloaded skills installer is not scanned here.

## Outstanding administration, legal and release work

This PR does not change GitHub settings and is **not full baseline compliance**.

- Private reporting was observed disabled. Enable it and confirm a working private
  route before changing the security policy to advertise one.
- Verify Dependabot alerts/security updates, secret scanning,
  push protection, access review and maintainer 2FA. Security settings were not
  exposed by the available API response; do not infer that they are enabled.
- Branch-protection inspection returned HTTP 403. Verify review requirements,
  CODEOWNERS enforcement and required checks after observing actual CI names.
  The local CODEOWNERS file is a review request, not enforcement or proof of access.
- Confirm authorship and any external origins of the original design text. Git
  history and declared Unlicense alone do not establish third-party clearance.
- There are no release assets today. Before publishing packaged releases, review
  their actual contents, preserve licenses/notices, and provide durable checksums
  and digest-bound provenance. Add both SBOM formats when component inventories
  apply; do not label this content manifest as a package SBOM.
- Central scan/check freshness monitoring and alerts older than 36 hours remain
  rollout work. Inspect the latest successful scheduled run in Actions; no claim
  of a successful nightly run is made before this workflow reaches `main`.
  Schedules can be delayed or disabled after inactivity.
