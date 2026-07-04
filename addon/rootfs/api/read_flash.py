from pathlib import Path
from threading import Thread

from fastapi import APIRouter
from pydantic import BaseModel

from core.jobs import manager
from esptool_api import run_esptool

router = APIRouter()

BACKUP_DIR = Path("/data/backups")
BACKUP_DIR.mkdir(parents=True, exist_ok=True)


class ReadFlashRequest(BaseModel):
    filename: str = "backup.bin"
    address: str = "0x0"
    size: str = "0x400000"


@router.post("/read_flash")
def read_flash(req: ReadFlashRequest):

    job = manager.create("read_flash")

    outfile = BACKUP_DIR / req.filename

    def worker():
        try:
            result = run_esptool(
                "read_flash",
                req.address,
                req.size,
                str(outfile),
            )

            if result["returncode"] == 0:
                result["file"] = str(outfile)
                manager.finish(job.id, result)
            else:
                manager.fail(job.id, result)

        except Exception as e:
            manager.fail(job.id, {"error": str(e)})

    Thread(target=worker, daemon=True).start()

    return {
        "job_id": job.id,
        "status": job.status,
    }


@router.get("/backups")
def backups():
    return [
        {
            "name": f.name,
            "size": f.stat().st_size,
        }
        for f in sorted(BACKUP_DIR.glob("*.bin"))
    ]
