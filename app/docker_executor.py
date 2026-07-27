import subprocess
import uuid
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SUBMISSIONS_ROOT = BASE_DIR / "submissions"
SHARED_VOLUME_ROOT = SUBMISSIONS_ROOT


def prepare_submission_workspace(code, submission_id, base_dir=None):
    root_dir = Path(base_dir) if base_dir else SUBMISSIONS_ROOT
    submission_dir = root_dir / submission_id
    submission_dir.mkdir(parents=True, exist_ok=True)

    source_path = submission_dir / "solution.py"
    source_path.write_text(code, encoding="utf-8")

    return str(submission_dir.resolve())


def write_submission_file(code, submission_id, base_dir=None):
    root_dir = Path(base_dir) if base_dir else SUBMISSIONS_ROOT
    submission_dir = root_dir / submission_id
    submission_dir.mkdir(parents=True, exist_ok=True)

    source_path = submission_dir / "solution.py"
    source_path.write_text(code, encoding="utf-8")
    try:
        source_path.chmod(0o666)
        submission_dir.chmod(0o777)
    except Exception:
        # chmod may fail on Windows - ignore
        pass

    # Also write to shared (host) submissions folder which will be mounted into the container at /code
    shared_dir = SHARED_VOLUME_ROOT / submission_id
    shared_dir.mkdir(parents=True, exist_ok=True)
    shared_file = shared_dir.joinpath("solution.py")
    shared_file.write_text(code, encoding="utf-8")
    try:
        shared_file.chmod(0o666)
        shared_dir.chmod(0o777)
    except Exception:
        pass

    return str(source_path.resolve())


def get_host_submission_path(submission_id):
    return str((SHARED_VOLUME_ROOT / submission_id / "solution.py").resolve())


def get_container_submission_path(submission_id):
    # inside the container submissions are available under /code/<id>/solution.py
    return f"/code/{submission_id}/solution.py"


def execute_python_docker(code, input_data=""):

    submission_id = str(uuid.uuid4())

    write_submission_file(code, submission_id)

    container_name = f"judge-{submission_id}"

    container_file_path = get_container_submission_path(
        submission_id
    )

    file_path = get_host_submission_path(
        submission_id
    )

    print("=" * 50)
    print("Submission ID:", submission_id)
    print("Container File Path:", container_file_path)
    print("Host File Path:", file_path)
    print("File Exists:", Path(file_path).exists())

    if Path(file_path).exists():
        print("File Content:")
        print(Path(file_path).read_text())

    print("=" * 50)

    try:

        print("Using Docker Volume: codingplatfrom_submissions-data")
        print("Container File Path:", container_file_path)

        result = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "--name",
                container_name,
                "--memory=128m",
                "--cpus=0.5",
                "--network=none",
                "-i",

                "--mount",
                "type=volume,source=codingplatfrom_submissions-data,target=/code",

                "code-runner",
                "python",
                container_file_path,
            ],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5,
        )

        print("=" * 50)
        print("Return Code:", result.returncode)
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)
        print("=" * 50)

        if result.returncode == 0:
            return result.stdout

        return result.stderr

    except subprocess.TimeoutExpired:
        print("Execution Timed Out")
        return "Time Limit Exceeded"

    except FileNotFoundError:
        print("Docker Engine Not Found")
        return "Docker engine is not available"

    except Exception as e:
        print("Unexpected Error:", str(e))
        return str(e)