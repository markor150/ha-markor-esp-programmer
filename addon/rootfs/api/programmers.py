from fastapi import APIRouter
from pydantic import BaseModel

from core.programmers import all, add

router = APIRouter()

class Programmer(BaseModel):
    name: str
    host: str
    port: int

@router.get("/programmers")
def programmers():
    return all()

@router.post("/programmers")
def programmer(p: Programmer):
    add(p.host, p.port, p.name)
    return {"success": True}
