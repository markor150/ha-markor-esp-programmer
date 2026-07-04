from pathlib import Path
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    dst = UPLOAD_DIR / file.filename
    with open(dst, "wb") as f:
        f.write(await file.read())
    return {
        "success": True,
        "filename": file.filename,
        "size": dst.stat().st_size,
    }

@router.get("/files")
def files():
    return [
        {
            "name": f.name,
            "size": f.stat().st_size,
        }
        for f in sorted(UPLOAD_DIR.glob("*.bin"))
    ]
