import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLANT_INFO_PATH = os.path.join(BASE_DIR, "plant_info.json")

def load_plant_info(plant_type=None):
    try:
        with open(PLANT_INFO_PATH, "r", encoding="utf-8") as f:
            info = json.load(f)
        if plant_type:
            return info.get(plant_type.lower(), None)
        return info
    except Exception as e:
        logging.error(f"Eroare la încărcarea plant_info.json: {e}")
        return None
