import gradio as gr
from app.model import EmotionRecognitionModel
from app.preprocessing import preprocess_audio
import os

model_path = os.path.join(os.path.dirname(__file__), '../models/trained_model_cnn_inc_res_nse_p-sh.h5')
model = EmotionRecognitionModel(model_path)

def predict_emotion(file_path):
    input_data = preprocess_audio(file_path)
    return model.predict(input_data)

iface = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Emotion Recognition with Inception-Residual CNN",
    description="Upload an audio file (WAV, MP3) to predict the emotion."
)

if __name__ == "__main__":
    iface.launch()