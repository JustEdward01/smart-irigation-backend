# app/routers/health.py
from fastapi import APIRouter
import logging
from app.services.db_service import supabase

router = APIRouter(prefix="/api", tags=["Health"])

@router.get("/health")
async def health_check():
    try:
        response = supabase.table("sensor_logs").select("*").limit(1).execute()
        if response.data is not None:
            db_status = "ok"
        else:
            db_status = "error"
    except Exception as e:
        logging.error(f"Eroare la verificarea bazei de date: {e}")
        db_status = "error"
    return {
        "api_status": "ok",
        "database_status": db_status,
        "message": "Backend-ul funcționează corect."
    }
@router.get("/ping", summary="Ping test endpoint", tags=["Health"])
async def ping():
    """
    Endpoint simplu pentru testarea funcționării API-ului.
    Returnează mesajul 'pong'.
    """
    return {"message": "pong"}