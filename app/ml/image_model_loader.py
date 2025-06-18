# app/ml/image_model_loader.py
import tensorflow as tf
import numpy as np

# Calea către modelul salvat pe HuggingFace sau local
MODEL_PATH = "https://huggingface.co/Eduard009/smartplant-model/resolve/main/symptom_cnn_model.h5"

# Poți folosi keras.utils.get_file dacă e online
plant_model = tf.keras.models.load_model(tf.keras.utils.get_file("symptom_model", MODEL_PATH))

plant_index_to_class = {
    0: "healthy",
    1: "yellow_leaves",
    2: "spots_mold",
    3: "wilting"
}

IMG_SIZE = (224, 224)

# Nu mai redefinim SYMPTOM_ACTION_MAP, îl importăm
from app.ml.symptom_action_map import SYMPTOM_ACTION_MAP
