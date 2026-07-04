from fastapi import APIRouter
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

