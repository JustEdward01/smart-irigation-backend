"""
Serviciu pentru procesarea și logarea datelor de la senzori.
Aici se face business logic (ex: salvare în DB, validare avansată, trimitere către ML).
"""
from app.models.sensor_data_model import SensorDataRequest, SensorDataResponse
from app.utils.logging_util import log_sensor_data  # exemplu, vezi utilitarul mai jos

# Dacă ai integrat Supabase, importă și clientul:
from app.services.db_service import supabase  # sau de unde ai create_client

def process_sensor_data(payload: SensorDataRequest) -> SensorDataResponse:
    """
    Procesează payload-ul de la senzori: logare, preprocesare, salvare.
    Poate apela logică ML/DB (mock aici, extensibil după caz).
    """
    log_sensor_data(payload.dict())
    # Exemplu cu salvare reală (dacă ai supabase):
    # supabase.table("sensor_logs").insert(payload.dict()).execute()
    return SensorDataResponse(
        status="success",
        message="Sensor data received and processed.",
        id=1
    )

def get_last_sensor_log():
    """
    Returnează ultimul log de la senzori din DB.
    """
    try:
        response = supabase.table("sensor_logs").select("*").order("timestamp", desc=True).limit(1).execute()
        if not response.data:
            return None
        return response.data[0]
    except Exception as e:
        # Dacă vrei să loghezi, folosește log_sensor_data sau logging direct
        print(f"Eroare la interogare senzori: {e}")
        return None

def save_sensor_data(data: dict):
    """
    Salvează date brute de la senzori (folosit pentru endpointul raw).
    """
    # Exemplu: salvezi în DB și returnezi dacă e nevoie udare imediată
    # supabase.table("sensor_logs").insert(data).execute()
    soil = data.get("soil_moisture", 100)
    water_now = soil < 35
    return {"water_now": water_now}
