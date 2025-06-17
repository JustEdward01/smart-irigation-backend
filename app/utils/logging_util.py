"""
Utilitar pentru logarea datelor primite de la senzori.
Aici pot fi adăugate și alte funcții pure, fără dependențe de FastAPI.
"""
import logging

def log_sensor_data(data: dict):
    logging.info(f"[SENSOR] Data received: {data}")
