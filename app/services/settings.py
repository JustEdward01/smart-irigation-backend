from app.models.settings import SystemConfig

def get_config() -> SystemConfig:
    return SystemConfig(
        selectedPlant="rosie",
        diagnosticFrequency="daily",
        alertThresholds={"moisture": 30, "light": 40, "temperature": {"min": 18, "max": 28}},
        systemSettings={"autoSync": True, "bufferSize": 5000, "logLevel": "info"}
    )

def set_config(config: SystemConfig):
    pass

def run_self_test():
    return {
        "sensors": {
            "moistureSensor": {"status": "ok", "value": "45%", "lastCheck": "2024-06-10"},
            "lightSensor": {"status": "ok", "value": "850 lux", "lastCheck": "2024-06-10"},
            "temperatureSensor": {"status": "warning", "value": "29°C", "lastCheck": "2024-06-10"},
            "phSensor": {"status": "error", "value": "N/A", "lastCheck": "2024-06-10"},
        },
        "connectivity": {
            "wifi": {"status": "ok", "signal": "-45 dBm"},
            "bluetooth": {"status": "ok", "connected": True},
        },
        "hardware": {
            "pump": {"status": "ok", "cycles": 1247},
            "led": {"status": "ok", "hours": 234},
            "battery": {"status": "ok", "level": "78%"},
            "storage": {"status": "warning", "usage": "87%"}
        }
    }

def get_system_info():
    return {
        "uptime": "7d 14h 32m",
        "firmwareVersion": "v2.1.3",
        "wifiStatus": "Conectat",
        "wifiSignal": -45,
        "batteryLevel": 78,
        "reservoirLevel": 65,
        "lastSync": "2 min ago"
    }
