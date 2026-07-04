import subprocess

from config import get_config


def run_esptool(*args, callback=None):

    cfg = get_config()

    cmd = [
        "python3",
        "-m",
        "esptool",
        "--port",
        f"rfc2217://{cfg['host']}:{cfg['port']}",
        *args,
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    output = []

    for line in process.stdout:
        line = line.rstrip()
        output.append(line)

        if callback:
            callback(line)

    process.wait()

    return {
        "host": cfg["host"],
        "port": cfg["port"],
        "returncode": process.returncode,
        "stdout": "\n".join(output),
        "stderr": "",
    }
