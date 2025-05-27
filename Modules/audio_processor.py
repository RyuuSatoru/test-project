# modules/audio_processor.py
import os
import torch
import torchaudio
import whisper

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium" if torch.cuda.is_available() else "base")# tiny-base-small-medium-large-(large-v2)

def process_audio(audio_path):
    result = model.transcribe(audio_path)
    transcript = result.get('text', '').strip()

    return {
        "path": audio_path,
        "transcript": transcript
    }
