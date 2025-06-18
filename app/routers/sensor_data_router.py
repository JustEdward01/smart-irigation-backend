from fastapi import APIRouter, Depends, Request, HTTPException
from app.utils.auth import verify_api_key
from app.services.sensor_data_service import get_last_sensor_log
import logging
import pandas as pd
from app.services.db_service import supabase
from app.ml.model_loader import load_models


router = APIRouter(prefix="/api", tags=["Sensor Data"])

@router.post("/predict", dependencies=[Depends(verify_api_key)])
async def predict_watering(data: dict, request: Request):
    try:
        input_dict = data
        plant_onehot = plant_type_encoder.transform(
            pd.DataFrame([[input_dict["plant_type"]]], columns=['plant_type'])
        )
        input_features = [
            input_dict["soil_moisture"],
            input_dict["temperature"],
            input_dict["air_humidity"],
            input_dict["light"],
            input_dict["last_watered_days"],
            input_dict["ml_prediction_prev"],
        ] + list(plant_onehot[0])
        columns = [
            'soil_moisture', 'temperature', 'air_humidity', 'light',
            'last_watered_days', 'ml_prediction_prev'
        ] + list(plant_type_encoder.get_feature_names_out(['plant_type']))
        input_df = pd.DataFrame([input_features], columns=columns)
        y_pred = multi_rf.predict(input_df)[0]
        water_given_ml, next_watering_days = y_pred

        log_entry = {
            **input_dict,
            "water_given_ml": float(water_given_ml),
            "next_watering_days": float(next_watering_days)
        }
        supabase.table("watering_logs").insert(log_entry).execute()

        return {
            "water_given_ml": round(float(water_given_ml), 1),
            "next_watering_days": round(float(next_watering_days), 1),
            "explanation": [
                f"Model ML pentru planta: {input_dict['plant_type']}."
            ],
            "source": "ML"
        }
    except Exception as e:
        logging.error(f"Eroare la ML predict: {e}")
        fallback = {
            "water_given_ml": 80.0 if data["soil_moisture"] < 30 else 0.0,
            "next_watering_days": 1 if data["soil_moisture"] < 30 else 3,
            "explanation": ["Fallback: ML nu a răspuns. Decizie bazată doar pe prag umiditate."],
            "source": "fallback"
        }
        return fallback

@router.get("/sensor-data", dependencies=[Depends(verify_api_key)])
async def get_sensor_data():
    try:
        data = get_last_sensor_log()
        if data is None:
            raise HTTPException(status_code=404, detail="No sensor data found")
        return data
    except Exception as e:
        logging.error(f"Exception in get_sensor_data: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")
