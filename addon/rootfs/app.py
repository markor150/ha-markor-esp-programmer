from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import subprocess

HOST = "192.168.1.126"
PORT = 3333

FIRMWARE_DIRS = [
    "/config/esphome/build",
    "/config/esphome",
]

app = FastAPI()


class FlashRequest(BaseModel):
    firmware: str


def find_firmwares():
    files = []
    for directory in FIRMWARE_DIRS:
        p = Path(directory)
        if p.exists():
            files.extend(p.rglob("*.bin"))
    return sorted(str(f) for f in files)


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


@app.get("/")
def root():
    return {"status": "ok", "name": "MarKor ESP Programmer"}


@app.get("/firmwares")
def firmwares():
    files = find_firmwares()
    return {
        "count": len(files),
        "files": files,
    }


@app.get("/flash_id")
def flash_id():
    return run_esptool("flash-id")


@app.get("/erase")
def erase():
    return run_esptool("erase-flash")


@app.post("/flash")
def flash(req: FlashRequest):
    if not Path(req.firmware).exists():
        return {
            "error": "Firmware not found",
            "path": req.firmware,
        }

    return run_esptool(
        "write-flash",
        "0x0",
        req.firmware,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8099)
