import joblib
import requests
from io import BytesIO

MODEL_URL = "https://huggingface.co/Eduard009/smartplant-model/resolve/main/smartplant_rf_model.joblib"
ENCODER_URL = "https://huggingface.co/Eduard009/smartplant-model/resolve/main/plant_type_encoder.joblib"

def load_models():
    model = joblib.load(BytesIO(requests.get(MODEL_URL).content))
    encoder = joblib.load(BytesIO(requests.get(ENCODER_URL).content))
    return model, encoder
plant_type_encoder = joblib.load("path/to/encoder.joblib")

# Exemplu de folosire:
# model, encoder = load_models()
