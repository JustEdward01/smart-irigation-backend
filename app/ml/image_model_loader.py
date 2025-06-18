import tensorflow as tf
from keras.layers import BatchNormalization
from keras.initializers import Zeros, Ones
from app.ml.symptom_action_map import SYMPTOM_ACTION_MAP

plant_index_to_class = {
    0: "healthy",
    1: "yellow_leaves",
    2: "spots_mold",
    3: "wilting"
}

IMG_SIZE = (224, 224)

# Path to the pre-trained model
MODEL_PATH = tf.keras.utils.get_file(
    "symptom_cnn_model.h5",
    "https://huggingface.co/Eduard009/smartplant-model/resolve/main/symptom_cnn_model.h5"
)

# Custom deserializer for BatchNormalization to handle axis stored as a list

def _bn_from_config(config):
    axis = config.get("axis")
    if isinstance(axis, (list, tuple)):
        config["axis"] = axis[0]
    return BatchNormalization.from_config(config)

# Load model with custom object to fix BatchNormalization deserialization
plant_model = tf.keras.models.load_model(
    MODEL_PATH,
    custom_objects={"BatchNormalization": _bn_from_config}
)