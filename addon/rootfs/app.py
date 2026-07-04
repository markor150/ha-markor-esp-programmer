from fastapi import FastAPI

from routes import router as core_router
from api.files import router as files_router
from api.flash import router as flash_router
from api.backup import router as backup_router

app = FastAPI(title="MarKor ESP Programmer")

app.include_router(core_router)
app.include_router(files_router)
app.include_router(flash_router)

app.include_router(backup_router)
