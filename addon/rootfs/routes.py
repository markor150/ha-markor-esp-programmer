from fastapi import APIRouter
from models import FlashRequest
from esptool_api import run_esptool

router = APIRouter()

@router.get("/")
def root():
    return {
        "status": "ok",
        "name": "MarKor ESP Programmer",
        "version": "0.1.0"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

@router.get("/flash_id")
def flash_id():
    return run_esptool("flash-id")

@router.get("/erase")
def erase():
    return run_esptool("erase-flash")

@router.post("/flash")
def flash(req: FlashRequest):
    return run_esptool(
        "write-flash",
        "0x0",
        req.firmware,
    )


@router.get("/chip_info")
def chip_info():
    return run_esptool("chip_id")


@router.get("/mac")
def mac():
    return run_esptool("read_mac")


@router.post("/erase")
def erase():
    return run_esptool("erase_flash")
