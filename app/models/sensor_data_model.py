from pydantic import BaseModel, Field, confloat, constr, validator
from typing import Optional
from datetime import datetime

class SensorDataRequest(BaseModel):
    plant_type: constr(strip_whitespace=True, min_length=1)
    soil_moisture: confloat(ge=0, le=100)
    temperature: confloat(ge=-20, le=60)
    light: confloat(ge=0, le=2000)
    battery: confloat(ge=2.0, le=4.3)
    timestamp: datetime

class SensorDataResponse(BaseModel):
    status: str
    message: str
    id: Optional[int] = None
