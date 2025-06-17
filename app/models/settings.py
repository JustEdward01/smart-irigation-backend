from pydantic import BaseModel

class SystemConfig(BaseModel):
    selectedPlant: str
    diagnosticFrequency: str
    alertThresholds: dict
    systemSettings: dict
