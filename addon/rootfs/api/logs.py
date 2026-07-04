from fastapi import APIRouter
from core.logs import get

router = APIRouter()

@router.get("/logs/{job_id}")
def logs(job_id: str):
    return {
        "job_id": job_id,
        "lines": get(job_id),
    }
