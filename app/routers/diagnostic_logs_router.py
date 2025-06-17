from fastapi import APIRouter, HTTPException, Body
# importă supabase, logging dacă nu ai deja
import logging
from app.services.db_service import supabase

router = APIRouter(tags=["Diagnostic Logs"])

@router.get("/api/diagnostic-logs")
async def get_diagnostic_logs(limit: int = 50):
    try:
        response = supabase.table("diagnostic_logs") \
            .select("*") \
            .order("timestamp", desc=True) \
            .limit(limit) \
            .execute()
        return response.data
    except Exception as e:
        logging.error(f"Eroare la get_diagnostic_logs: {e}")
        raise HTTPException(status_code=500, detail="Eroare la interogare diagnostic logs")

@router.patch("/api/diagnostic-logs/{log_id}/feedback")
async def update_diagnostic_feedback(log_id: str, user_feedback: str = Body(..., embed=True)):
    try:
        response = supabase.table("diagnostic_logs") \
            .update({"user_feedback": user_feedback}) \
            .eq("id", log_id) \
            .execute()
        if response.data:
            return {"message": "Feedback salvat", "log": response.data[0]}
        else:
            raise HTTPException(status_code=404, detail="Log not found")
    except Exception as e:
        logging.error(f"Eroare la update_diagnostic_feedback: {e}")
        raise HTTPException(status_code=500, detail="Eroare la update feedback")
