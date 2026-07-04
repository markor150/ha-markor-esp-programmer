from fastapi import APIRouter
from pydantic import BaseModel

from esptool_api import run_esptool

router = APIRouter()


class FlashRequest(BaseModel):
    filename: str
    address: str = "0x0"
    baud: int = 460800
    verify: bool = True


@router.post("/flash")
def flash(req: FlashRequest):

    args = [
        "--baud",
        str(req.baud),
        "write_flash",
        req.address,
        f"/data/uploads/{req.filename}",
    ]

    if req.verify:
        args.insert(0, "--verify")

    return run_esptool(*args)
