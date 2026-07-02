import subprocess
from pathlib import Path

SAFE_COMMANDS = {
    "make smoke": ["make", "smoke"],
    "make test": ["make", "test"],
    "git diff": ["git", "diff"],
    "git status": ["git", "status", "--short"],
}

def run_safe_command(command_name: str, cwd: str = ".") -> dict:
    if command_name not in SAFE_COMMANDS:
        return {
            "ok": False,
            "stdout": "",
            "stderr": f"Command not allowed without explicit approval: {command_name}",
            "returncode": 126,
        }

    proc = subprocess.run(
        SAFE_COMMANDS[command_name],
        cwd=Path(cwd),
        text=True,
        capture_output=True,
        timeout=120,
    )
    return {
        "ok": proc.returncode == 0,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "returncode": proc.returncode,
    }
