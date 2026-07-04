from fastapi import FastAPI

from routes import router as core_router
from api.files import router as files_router
from api.flash import router as flash_router
from api.jobs import router as jobs_router
from api.device import router as device_router
from api.logs import router as logs_router
from api.progress import router as progress_router
from api.detect import router as detect_router
from api.read_flash import router as read_flash_router
from api.device_info import router as device_info_router
from api.programmers import router as programmers_router
from api.backup import router as backup_router

app = FastAPI(title="MarKor ESP Programmer")

app.include_router(core_router)
app.include_router(files_router)
app.include_router(flash_router)

app.include_router(backup_router)
