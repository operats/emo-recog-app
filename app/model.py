import tensorflow as tf
import numpy as np

class EmotionRecognitionModel:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.emo_label_mapping = {
            0: "Neutral",
            1: "Happy",
            2: "Sad",
            3: "Angry",
            4: "Fearful",
            5: "Disgust"
        }

    def predict(self, input_data):
        predictions = self.model.predict(input_data)
        predicted_class = np.argmax(predictions, axis=1)[0]
        return self.emo_label_mapping.get(predicted_class, "Unknown Emotion")