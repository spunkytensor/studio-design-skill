import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.check_content import CONTENT, POLICY, SKILL, check


class ContentChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[1]
        self.tracked = sorted(CONTENT | POLICY)
        for name in self.tracked:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, target)

    def update_hash(self, name):
        path = self.root / "content-inventory.json"
        inventory = json.loads(path.read_text())
        inventory["files"][name]["sha256"] = hashlib.sha256((self.root / name).read_bytes()).hexdigest()
        path.write_text(json.dumps(inventory))

    def test_reviewed_content_passes(self):
        check(self.root, self.tracked)

    def test_nested_dependency_or_asset_requires_review(self):
        for extra in (f"{SKILL}/package.json", f"{SKILL}/font.woff2"):
            with self.subTest(extra=extra), self.assertRaisesRegex(ValueError, "profile needs review"):
                check(self.root, self.tracked + [extra])

    def test_missing_distributed_file_fails(self):
        self.tracked.remove(f"{SKILL}/UNLICENSE")
        with self.assertRaisesRegex(ValueError, "missing="):
            check(self.root, self.tracked)

    def test_content_change_requires_review(self):
        (self.root / SKILL / "SKILL.md").write_text("unreviewed copied content")
        with self.assertRaisesRegex(ValueError, "Content changed"):
            check(self.root, self.tracked)

    def test_license_mismatch_even_with_updated_hash(self):
        name = f"{SKILL}/UNLICENSE"
        (self.root / name).write_text("Different terms")
        self.update_hash(name)
        with self.assertRaisesRegex(ValueError, "Bundled Unlicense differs"):
            check(self.root, self.tracked)

    def test_missing_provenance_fails(self):
        path = self.root / "content-inventory.json"
        inventory = json.loads(path.read_text())
        inventory["files"]["README.md"]["origin"] = " "
        path.write_text(json.dumps(inventory))
        with self.assertRaisesRegex(ValueError, "Missing license/provenance"):
            check(self.root, self.tracked)

    def test_incomplete_inventory_fails(self):
        path = self.root / "content-inventory.json"
        inventory = json.loads(path.read_text())
        del inventory["files"]["UNLICENSE"]
        path.write_text(json.dumps(inventory))
        with self.assertRaisesRegex(ValueError, "exactly the distributed content"):
            check(self.root, self.tracked)

    def test_broken_local_link_fails(self):
        (self.root / "SECURITY.md").write_text("[report](missing.md)")
        with self.assertRaisesRegex(ValueError, "Broken or escaping local link"):
            check(self.root, self.tracked)

    def test_symlink_fails(self):
        path = self.root / "SECURITY.md"
        path.unlink()
        path.symlink_to("README.md")
        with self.assertRaisesRegex(ValueError, "Not a regular in-tree file"):
            check(self.root, self.tracked)

    def test_skill_identity_even_with_updated_hash(self):
        name = f"{SKILL}/SKILL.md"
        path = self.root / name
        path.write_text(path.read_text().replace("name: designing-translucent-interfaces", "name: wrong-name"))
        self.update_hash(name)
        with self.assertRaisesRegex(ValueError, "Skill identity"):
            check(self.root, self.tracked)


if __name__ == "__main__":
    unittest.main()
