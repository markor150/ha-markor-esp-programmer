from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from firmware.manager import FirmwareManager

router = APIRouter()

UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

manager = FirmwareManager()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    dst = UPLOAD_DIR / file.filename

    with open(dst, "wb") as fp:
        fp.write(await file.read())

    return {
        "success": True,
        "filename": file.filename,
        "size": dst.stat().st_size,
    }


@router.get("/files")
def files():
    return manager.scan()


@router.get("/files/{filename}")
def file_info(filename: str):
    file = UPLOAD_DIR / filename

    if not file.exists():
        return {"success": False}

    return {
        "success": True,
        "name": file.name,
        "size": file.stat().st_size,
        "path": str(file),
    }


@router.delete("/files/{filename}")
def delete_file(filename: str):
    file = UPLOAD_DIR / filename

    if not file.exists():
        return {"success": False}

    file.unlink()

    return {
        "success": True,
        "deleted": filename,
    }


@router.post("/files/refresh")
def refresh():
    return {
        "success": True,
        "count": len(manager.scan()),
        "files": manager.scan(),
    }
