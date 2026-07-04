from threading import Thread

from fastapi import APIRouter
from pydantic import BaseModel

from core.jobs import manager
from esptool_api import run_esptool

router = APIRouter()


class FlashRequest(BaseModel):
    filename: str
    address: str = "0x0"
    baud: int = 460800


@router.post("/flash")
def flash(req: FlashRequest):

    job = manager.create("flash")

    def worker():
        try:
            result = run_esptool(
                "--baud",
                str(req.baud),
                "write_flash",
                req.address,
                f"/data/uploads/{req.filename}",
            )

            if result["returncode"] == 0:
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
