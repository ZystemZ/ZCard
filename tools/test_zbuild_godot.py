import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("zbuild-godot.py")
SPEC = importlib.util.spec_from_file_location("zbuild_godot", SCRIPT)
zbuild = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(zbuild)


class TargetParsingTests(unittest.TestCase):
    def test_dual_expands_to_windows_and_linux(self):
        self.assertEqual(zbuild.parse_targets("dual"), ["windows", "linux"])

    def test_all_expands_and_deduplicates(self):
        self.assertEqual(zbuild.parse_targets("windows,all"), ["windows", "linux", "android"])

    def test_unknown_target_is_rejected(self):
        with self.assertRaises(zbuild.BuildError):
            zbuild.parse_targets("switch")


class PackageTests(unittest.TestCase):
    def test_zip_is_valid_and_contains_manifest(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "stage"
            (root / "META").mkdir(parents=True)
            (root / "META" / "zgame.json").write_text('{"format":"zgame-0.1"}', encoding="utf-8")
            output = Path(temporary) / "game.zcard"
            zbuild.write_deterministic_zip(root, output)
            with zipfile.ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn("META/zgame.json", archive.namelist())

    def test_zip_output_is_deterministic(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "stage"
            (root / "META").mkdir(parents=True)
            (root / "META" / "zgame.json").write_text("{}", encoding="utf-8")
            first = Path(temporary) / "first.zcard"
            second = Path(temporary) / "second.zcard"
            zbuild.write_deterministic_zip(root, first)
            zbuild.write_deterministic_zip(root, second)
            self.assertEqual(zbuild.sha256_file(first), zbuild.sha256_file(second))


if __name__ == "__main__":
    unittest.main()
