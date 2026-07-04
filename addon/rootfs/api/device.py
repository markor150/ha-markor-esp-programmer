from threading import Thread

from fastapi import APIRouter

from core.jobs import manager
from esptool_api import run_esptool

router = APIRouter()


def start_job(action, *args):

    job = manager.create(action)

    def worker():
        try:
            result = run_esptool(*args)

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


@router.get("/flash_id")
def flash_id():
    return start_job("flash_id", "flash-id")


@router.get("/chip_info")
def chip_info():
    return start_job("chip_info", "chip_id")


@router.get("/mac")
def mac():
    return start_job("read_mac", "read_mac")


@router.post("/erase")
def erase():
    return start_job("erase", "erase_flash")
