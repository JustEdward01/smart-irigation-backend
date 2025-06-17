# app/services/wifi.py

import os

def get_wifi_status():
    """
    Returnează statusul WiFi-ului sistemului.
    Poți integra aici logica de citire din hardware, OS, sau pur și simplu returnezi mock/demo pentru început.
    """
    # Exemplu mock (de modificat cu status real dacă vrei)
    return {
        "connected": True,
        "ssid": os.getenv("WIFI_SSID", "SmartPlant-NET"),
        "ip": os.getenv("WIFI_IP", "192.168.1.101"),
    }

def reset_wifi():
    """
    Trimite comandă de reset la conexiunea WiFi a sistemului.
    Poți implementa fie cu comenzi OS, fie cu comunicare serială spre hardware, sau doar mock (pentru demo/dev).
    """
    # Exemplu mock: întotdeauna succes.
    return True
