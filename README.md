# Emotion Recognition App

## Getting Started

1. Clone the repository: `git clone https://github.com/operats/emo-recog-app.git`
2. Navigate to the repository: `cd emo-recog-app`
3. Make the script executable: `chmod +x run.sh`
4. Run the app: `./run.sh`
5. Open a web browser and navigate to the URL provided in the terminal output.

## Testing with Sample Audio Files

I've provided a directory `data/unseen_data` with some sample audio files (WAV format) for you to test the model. To use these files:

1. Make sure the `data/unseen_data` directory is in the same directory as the Gradio app.
2. In the Gradio app, click on the "Audio" input field and select one of the WAV files from the `data/unseen_data` directory.
3. Click the "Submit" button to upload the file and get the predicted emotion.

## Folder structure
```
emotion-recognition-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── preprocessing.py
├── data/
│   └── unseen_data/
│       ├── audio_file1.wav
│       ├── audio_file2.wav
│       └── ...
├── models/
│   └── trained_model_cnn_inc_res_nse_p-sh.h5
├── .gitignore
├── README.md
├── requirements.txt
└── run.sh
```
## Model details

