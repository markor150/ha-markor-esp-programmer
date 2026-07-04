from pathlib import Path
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def scan_uploads():
    result = []

    for f in sorted(UPLOAD_DIR.glob("*.bin")):
        result.append(
            {
                "name": f.name,
                "size": f.stat().st_size,
                "source": "upload",
                "path": str(f),
            }
        )

    return result


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
    return scan_uploads()


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
        "count": len(scan_uploads()),
        "files": scan_uploads(),
    }
