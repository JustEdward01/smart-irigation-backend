# app/routers/system_status_router.py

from fastapi import APIRouter

router = APIRouter(tags=["System Status"])

@router.get("/api/system-status")
def system_status():
    return {"status": "ok"}
