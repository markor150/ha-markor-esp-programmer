import subprocess
from config import get_config


def run_esptool(*args):
    cfg = get_config()

    cmd = [
        "python3",
        "-m",
        "esptool",
        "--port",
        f"rfc2217://{cfg['host']}:{cfg['port']}",
        *args,
    ]

    r = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )

    return {
        "host": cfg["host"],
        "port": cfg["port"],
        "returncode": r.returncode,
        "stdout": r.stdout,
        "stderr": r.stderr,
    }
