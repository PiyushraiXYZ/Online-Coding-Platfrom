import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app import docker_executor
from app.docker_executor import prepare_submission_workspace, write_submission_file


class PrepareSubmissionWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="submission-test-", dir=".")
        self.addCleanup(shutil.rmtree, self.temp_dir, ignore_errors=True)

    def test_prepares_submission_directory_and_writes_source_file(self):
        submission_id = "submission-123"
        code = "print('hello')\n"

        workspace_dir = prepare_submission_workspace(
            code=code,
            submission_id=submission_id,
            base_dir=self.temp_dir,
        )

        self.assertTrue(Path(workspace_dir).exists())
        self.assertTrue((Path(workspace_dir) / "solution.py").exists())
        self.assertEqual((Path(workspace_dir) / "solution.py").read_text(encoding="utf-8"), code)

    def test_write_submission_file_mirrors_code_to_shared_volume(self):
        submission_id = "submission-456"
        code = "print('shared')\n"
        shared_root = Path(self.temp_dir) / "shared"
        shared_root.mkdir(parents=True, exist_ok=True)

        with patch.object(docker_executor, "SHARED_VOLUME_ROOT", shared_root):
            written_path = write_submission_file(code=code, submission_id=submission_id, base_dir=self.temp_dir)

        self.assertTrue(Path(written_path).exists())
        self.assertTrue((shared_root / submission_id / "solution.py").exists())
        self.assertEqual((shared_root / submission_id / "solution.py").read_text(encoding="utf-8"), code)


if __name__ == "__main__":
    unittest.main()
