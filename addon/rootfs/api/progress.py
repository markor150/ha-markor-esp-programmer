from fastapi import APIRouter
from core.progress import get

router = APIRouter()

@router.get("/progress/{job_id}")
def progress(job_id: str):
    return get(job_id)
