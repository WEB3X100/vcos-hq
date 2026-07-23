#!/usr/bin/env python3
"""
Unit tests for L2 Mission Preflight Validator.
Uses temporary Git repositories. Stdlib only.
"""

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

# Import the validator module
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from l2_mission_preflight import validate, FAST_PATH_FILES


def init_temp_git_repo():
    """Create a temp dir, init git, return Path."""
    tmp = tempfile.mkdtemp()
    tmp_path = Path(tmp)
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=tmp_path, check=True)
    return tmp_path


def create_fast_path_files(root: Path):
    """Create the four mandatory fast-path files with minimal content."""
    for rel in FAST_PATH_FILES:
        full = root / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text("# placeholder\n", encoding="utf-8")


class TestL2Preflight(unittest.TestCase):

    def setUp(self):
        self.temp_dirs = []

    def tearDown(self):
        for d in self.temp_dirs:
            shutil.rmtree(d, ignore_errors=True)

    def _new_repo(self):
        d = init_temp_git_repo()
        self.temp_dirs.append(d)
        return d

    def test_valid_clean_l2_branch_passes(self):
        repo = self._new_repo()
        # Create branch l2/test
        subprocess.run(["git", "checkout", "-q", "-b", "l2/test"], cwd=repo, check=True)
        create_fast_path_files(repo)
        # Commit the files so tree is clean
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)
        # Add origin/main simulation (simple tag or just ensure origin/main ref exists for ahead/behind)
        # For test, create a dummy origin/main by committing on main first then branching
        # Simpler: just run validate - it should pass on clean l2/ with files
        rc = validate(cwd=str(repo), json_output=False)
        self.assertEqual(rc, 0)

    def test_main_branch_fails(self):
        repo = self._new_repo()
        create_fast_path_files(repo)
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)
        # Stay on main
        rc = validate(cwd=str(repo), json_output=False)
        self.assertEqual(rc, 1)

    def test_missing_fast_path_fails(self):
        repo = self._new_repo()
        subprocess.run(["git", "checkout", "-q", "-b", "l2/test"], cwd=repo, check=True)
        # Create a dummy commit so we can have a clean tree without fast-path files
        (repo / "dummy.txt").write_text("dummy", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)
        rc = validate(cwd=str(repo), json_output=False)
        self.assertEqual(rc, 1)

    def test_tracked_private_file_fails(self):
        repo = self._new_repo()
        subprocess.run(["git", "checkout", "-q", "-b", "l2/test"], cwd=repo, check=True)
        create_fast_path_files(repo)
        # Create and track a private path
        (repo / ".hermes" / "config").parent.mkdir(exist_ok=True)
        (repo / ".hermes" / "config").write_text("secret", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)
        rc = validate(cwd=str(repo), json_output=False)
        self.assertEqual(rc, 1)

    def test_dirty_tree_fails(self):
        repo = self._new_repo()
        subprocess.run(["git", "checkout", "-q", "-b", "l2/test"], cwd=repo, check=True)
        create_fast_path_files(repo)
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)
        # Make it dirty
        (repo / "dirty.txt").write_text("change", encoding="utf-8")
        rc = validate(cwd=str(repo), json_output=False)
        self.assertEqual(rc, 1)

    def test_json_output_parses(self):
        repo = self._new_repo()
        subprocess.run(["git", "checkout", "-q", "-b", "l2/test"], cwd=repo, check=True)
        create_fast_path_files(repo)
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True)
        # Capture JSON
        import io
        import contextlib
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        try:
            rc = validate(cwd=str(repo), json_output=True)
        finally:
            sys.stdout = old_stdout
        output = mystdout.getvalue()
        data = json.loads(output)
        self.assertEqual(data["status"], "PASS")
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
