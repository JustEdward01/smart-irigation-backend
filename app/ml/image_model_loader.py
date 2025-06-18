import tensorflow as tf
from app.ml.symptom_action_map import SYMPTOM_ACTION_MAP
from keras.layers import BatchNormalization

def _bn_from_config(config):
    # Dacă axis e listă, reține doar primul element
    axis = config.get("axis")
    if isinstance(axis, (list, tuple)):
        config["axis"] = axis[0]
    return BatchNormalization.from_config(config)

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

- plant_model = tf.keras.models.load_model(MODEL_PATH)
+ plant_model = tf.keras.models.load_model(
+     MODEL_PATH,custom_objects={"BatchNormalization": _bn_from_config})
