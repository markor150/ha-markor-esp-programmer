from fastapi import APIRouter, HTTPException

from core.jobs import manager

router = APIRouter()

@router.get("/jobs")
def jobs():
    return [
        {
            "id": j.id,
            "action": j.action,
            "status": j.status,
            "created": j.created,
        }
        for j in manager.list()
    ]

@router.get("/jobs/{job_id}")
def job(job_id: str):
    j = manager.get(job_id)

    if j is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "id": j.id,
        "action": j.action,
        "status": j.status,
        "created": j.created,
        "result": j.result,
    }
