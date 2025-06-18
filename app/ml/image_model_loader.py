# app/ml/image_model_loader.py
import tensorflow as tf
import numpy as np
from app.ml.symptom_action_map import SYMPTOM_ACTION_MAP

# Descărcare și salvare locală (doar dacă nu există deja)
MODEL_PATH = tf.keras.utils.get_file(
    "symptom_cnn_model.h5",
    "https://huggingface.co/Eduard009/smartplant-model/resolve/main/symptom_cnn_model.h5"
)

# Încărcare model h5 (compatibil Keras 3)
plant_model = tf.keras.models.load_model(MODEL_PATH)

# Alte constante
plant_index_to_class = {
    0: "healthy",
    1: "yellow_leaves",
    2: "spots_mold",
    3: "wilting"
}
IMG_SIZE = (224, 224)
