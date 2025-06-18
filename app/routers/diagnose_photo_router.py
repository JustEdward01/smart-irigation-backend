from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from app.utils.auth import verify_api_key

from app.ml.image_model_loader import plant_model, plant_index_to_class, IMG_SIZE, SYMPTOM_ACTION_MAP
from app.services.db_service import supabase

from PIL import Image
import io
import numpy as np
import logging
from datetime import datetime

router = APIRouter(tags=["Diagnose Photo"])

@router.post("/api/diagnose-photo", dependencies=[Depends(verify_api_key)])
async def diagnose_photo(file: UploadFile = File(...), plant_type: str = None):
    try:
        if plant_model is None or plant_index_to_class is None:
            raise HTTPException(status_code=500, detail="Modelul AI nu este încărcat.")

        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert("RGB")
        img = img.resize(IMG_SIZE)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        preds = plant_model.predict(img_array)
        pred_index = int(np.argmax(preds))
        confidence = float(np.max(preds))
        predicted_class = plant_index_to_class[pred_index]

        mapping = SYMPTOM_ACTION_MAP.get(predicted_class, SYMPTOM_ACTION_MAP["unknown"])
        adjust_days = mapping["adjust_watering_days"]
        reduce_ml = mapping["reduce_water_ml"]
        decision_reason = f"Ajustare automată: detectat simptom '{predicted_class}' cu scor {confidence:.2f}. {mapping['notify_user']}"

        log_entry = {
            "plant_type": plant_type,
            "img_path": None,
            "predicted_class": predicted_class,
            "confidence": confidence,
            "action_message": mapping["notify_user"],
            "adjust_days": adjust_days,
            "reduce_ml": reduce_ml,
            "all_scores": {plant_index_to_class[i]: float(score) for i, score in enumerate(preds[0])},
            "decision_reason": decision_reason,
            "timestamp": datetime.utcnow().isoformat(),
        }
        try:
            supabase.table("diagnostic_logs").insert(log_entry).execute()
        except Exception as db_err:
            logging.error(f"Eroare la logare diagnostic_logs: {db_err}")

        return {
            "predicted_class": predicted_class,
            "confidence": confidence,
            "all_scores": {plant_index_to_class[i]: float(score) for i, score in enumerate(preds[0])},
            "action_message": mapping["notify_user"],
            "adjust_days": adjust_days,
            "reduce_ml": reduce_ml,
            "decision_reason": decision_reason
        }
    except Exception as e:
        logging.error(f"Eroare la diagnose-photo: {e}")
        raise HTTPException(status_code=500, detail=str(e))
