from fastapi import APIRouter, HTTPException
# importă supabase, logging dacă nu ai deja
from app.services.db_service import supabase
import logging

router = APIRouter(tags=["History"])

@router.get("/history")
def get_history(limit: int = 20):
    try:
        response = supabase.table("sensor_logs").select("*").order("timestamp", desc=True).limit(limit).execute()
        logging.info("History request - success")
        return response.data
    except Exception as e:
        logging.error(f"Eroare la history: {e}")
        raise HTTPException(status_code=500, detail="Eroare la interogare istoric")

@router.get("/api/history")
def get_watering_history(limit: int = 100):
    try:
        response = supabase.table("watering_logs").select("*").order("timestamp", desc=True).limit(limit).execute()
        logging.info("Watering history request - success")
        return response.data
    except Exception as e:
        logging.error(f"Eroare la watering_history: {e}")
        raise HTTPException(status_code=500, detail="Eroare la interogare istoric udări")
