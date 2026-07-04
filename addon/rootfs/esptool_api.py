import subprocess
from config import HOST, PORT

def run_esptool(*args):
    cmd = [
        "python3",
        "-m",
        "esptool",
        "--port",
        f"rfc2217://{HOST}:{PORT}",
        *args,
    ]

    r = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )

    return {
        "returncode": r.returncode,
        "stdout": r.stdout,
        "stderr": r.stderr,
    }
