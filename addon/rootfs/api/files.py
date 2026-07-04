from pathlib import Path
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ESPHOME_BUILD = Path("/share/markor")


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
    result = []

    # Uploads
    for f in sorted(UPLOAD_DIR.glob("*.bin")):
        result.append({
            "name": f.name,
            "size": f.stat().st_size,
            "source": "upload",
            "path": str(f),
        })

    # ESPHome build
    if ESPHOME_BUILD.exists():
        for fw in sorted(ESPHOME_BUILD.glob("*/.pioenvs/*/firmware*.bin")):
            device = fw.parents[2].name

            result.append({
                "name": f"{device}/{fw.name}",
                "size": fw.stat().st_size,
                "source": "esphome",
                "path": str(fw),
            })

    return sorted(result, key=lambda x: (x["source"], x["name"]))
