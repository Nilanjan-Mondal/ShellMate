import subprocess

def safe_execute(command: str, dry: bool = True) -> dict:
    if dry:
        return {"executed": False, "command": command}
    try:
        proc = subprocess.run(
            command, shell=True, check=False,
            capture_output=True, text=True, executable="/bin/bash"
        )
        return {
            "executed": True,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
    except Exception as exc:
        return {"executed": False, "error": str(exc)}
