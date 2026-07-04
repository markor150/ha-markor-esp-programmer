from fastapi import FastAPI
import subprocess

app = FastAPI()

HOST="192.168.1.126"
PORT=3333

@app.get("/flash_id")
def flash_id():
    cmd=[
        "python3","-m","esptool",
        "--port",
        f"rfc2217://{HOST}:{PORT}",
        "flash-id"
    ]

    r=subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return {
        "returncode":r.returncode,
        "stdout":r.stdout,
        "stderr":r.stderr
    }
