from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.services.logs import export_logs

router = APIRouter(prefix="/api/logs", tags=["logs"])

@router.get("/export")
def logs_export():
    logs_txt = export_logs()
    return PlainTextResponse(logs_txt)
