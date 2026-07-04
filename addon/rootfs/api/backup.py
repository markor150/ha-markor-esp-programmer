from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

from esptool_api import run_esptool

router = APIRouter()

BACKUP_DIR = Path("/data/backups")
BACKUP_DIR.mkdir(parents=True, exist_ok=True)


class BackupRequest(BaseModel):
    filename: str = "backup.bin"
    address: str = "0x000000"
    size: str = "0x400000"


@router.post("/backup")
def backup(req: BackupRequest):

    outfile = BACKUP_DIR / req.filename

    return run_esptool(
        "read_flash",
        req.address,
        req.size,
        str(outfile),
    )


@router.get("/backups")
def backups():

    return [
        {
            "name": f.name,
            "size": f.stat().st_size,
        }
        for f in sorted(BACKUP_DIR.glob("*.bin"))
    ]
