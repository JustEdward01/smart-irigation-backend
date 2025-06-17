# app/services/system_service.py
"""
Logica pentru setarea credentialelor WiFi și status sistem.
"""

import serial
import socket
from app.models.system_model import WiFiCreds, SystemStatusResponse
import os

def set_wifi_creds(creds: WiFiCreds) -> dict:
    """
    Trimite datele de WiFi către hardware prin UART sau altă metodă.
    """
    try:
        # Înlocuiește 'COMx' cu portul real, adaptează baudrate dacă trebuie!
        ser = serial.Serial('COMx', 115200, timeout=1)
        cmd = f"{creds.ssid},{creds.password}\n"
        ser.write(cmd.encode())
        ser.close()
        return {"status": "ok"}
    except Exception as e:
        # Propagă excepția către router
        raise RuntimeError(f"Failed to set WiFi: {e}")

def get_system_status() -> SystemStatusResponse:
    """
    Returnează statusul conexiunii sistemului (mock sau real).
    """
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        ssid = os.getenv("WIFI_SSID", "Unknown")
        return SystemStatusResponse(
            connected=True,
            ssid=ssid,
            ip=ip
        )
    except Exception:
        return SystemStatusResponse(connected=False)
