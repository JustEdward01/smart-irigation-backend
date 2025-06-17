multi_rf = joblib.load("smartplant_rf_model.joblib")
plant_type_encoder = joblib.load("plant_type_encoder.joblib")
MODEL_PATH = 'plant_diagnosis_final.keras'
LABEL_MAP_PATH = 'label_map.json'
PLANT_INFO_PATH = 'plant_info.json'
IMG_SIZE = (224, 224)

try:
    plant_model = tf.keras.models.load_model(MODEL_PATH)
    with open(LABEL_MAP_PATH) as f:
        plant_label_map = json.load(f)
    plant_index_to_class = {v: k for k, v in plant_label_map.items()}
    print("Model AI vizual încărcat OK")
except Exception as e:
    plant_model = None
    plant_label_map = None
    plant_index_to_class = None
    logging.error(f"Eroare la încărcarea modelului vizual: {e}")
