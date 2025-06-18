import tensorflow as tf
from app.ml.symptom_action_map import SYMPTOM_ACTION_MAP

plant_index_to_class = {
    0: "healthy",
    1: "yellow_leaves",
    2: "spots_mold",
    3: "wilting"
}

IMG_SIZE = (224, 224)

MODEL_PATH = tf.keras.utils.get_file(
    "symptom_cnn_model.h5",
    "https://huggingface.co/Eduard009/smartplant-model/resolve/main/symptom_cnn_model.h5"
)

plant_model = tf.keras.models.load_model(MODEL_PATH)
