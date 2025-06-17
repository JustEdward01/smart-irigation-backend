from pydantic import BaseModel, Field, conint
from typing import Optional

class PredictRequest(BaseModel):
    plant_type: str
    soil_moisture: float = Field(..., ge=0, le=100)
    temperature: float
    air_humidity: float = Field(..., ge=0, le=100)
    light: float
    last_watered_days: Optional[conint(ge=0)] = None
    ml_prediction_prev: Optional[float] = None
