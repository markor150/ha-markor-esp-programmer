from threading import Thread

from fastapi import APIRouter

from core.jobs import manager
from esptool_api import run_esptool

router = APIRouter()

@router.get("/detect")
def detect():

    job = manager.create("detect")

    def worker():
        try:
            result = run_esptool("chip_id")

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
