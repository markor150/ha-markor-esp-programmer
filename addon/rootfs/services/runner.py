from threading import Thread

from core.jobs import manager
from esptool_api import run_esptool


def run_job(action, *args):

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
