import librosa
import numpy as np

def preprocess_audio(file_path, target_sr=16000, target_size=(128, 128)):
    """Loads and preprocesses an audio file."""
    audio, sr = librosa.load(file_path, sr=target_sr)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)  

    mfcc_resized = np.array(librosa.util.fix_length(mfccs, size=target_size[1]))  
    mfcc_resized = np.resize(mfcc_resized, (target_size[0], target_size[1]))  

    mfcc_resized = np.expand_dims(mfcc_resized, axis=-1)  
    return np.expand_dims(mfcc_resized, axis=0)  