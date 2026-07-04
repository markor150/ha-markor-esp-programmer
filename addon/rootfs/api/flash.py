from fastapi import APIRouter
from pydantic import BaseModel

from esptool_api import run_esptool

router = APIRouter()

class FlashRequest(BaseModel):
    filename: str
    address: str = "0x0"
    baud: int = 460800

@router.post("/flash")
def flash(req: FlashRequest):
    return run_esptool(
        "--baud",
        str(req.baud),
        "write_flash",
        req.address,
        f"/data/uploads/{req.filename}",
    )
