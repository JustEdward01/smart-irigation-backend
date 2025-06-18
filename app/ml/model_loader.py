import joblib
import os
import requests
from io import BytesIO

MODEL_URL = "https://huggingface.co/Eduard009/smartplant-model/resolve/main/smartplant_rf_model.joblib"
ENCODER_URL = "https://huggingface.co/Eduard009/smartplant-model/resolve/main/plant_type_encoder.joblib"

CACHE_DIR = "/tmp/model_cache"
MODEL_PATH = os.path.join(CACHE_DIR, "smartplant_rf_model.joblib")
ENCODER_PATH = os.path.join(CACHE_DIR, "plant_type_encoder.joblib")

def download_file(url, path):
    if not os.path.exists(path):
        print(f"Downloading {url}...")
        response = requests.get(url)
        response.raise_for_status()
        with open(path, "wb") as f:
            f.write(response.content)

def load_models():
    os.makedirs(CACHE_DIR, exist_ok=True)
    download_file(MODEL_URL, MODEL_PATH)
    download_file(ENCODER_URL, ENCODER_PATH)

    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return encoder, model
