from fastapi import APIRouter, HTTPException
from app.services.wifi import get_wifi_status, reset_wifi

router = APIRouter(prefix="/api/wifi", tags=["wifi"])

@router.get("/status")
def wifi_status():
    return get_wifi_status()

@router.post("/reset")
def wifi_reset():
    if not reset_wifi():
        raise HTTPException(status_code=500, detail="Reset WiFi eșuat.")
    return {"message": "Reset WiFi trimis."}
