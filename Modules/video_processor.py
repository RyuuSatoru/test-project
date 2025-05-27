import os
import moviepy.editor as mp
import whisper
import torch
import cv2
from ultralytics import YOLO
from collections import Counter

def extract_transcript(video_path):
    video = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.wav"

    if video.audio is None:
        return ""

    video.audio.write_audiofile(audio_path, verbose=False, logger=None)

    model = whisper.load_model("base" if torch.cuda.is_available() else "tiny")
    result = model.transcribe(audio_path)
    os.remove(audio_path)

    transcript = result['text'].strip()
    return transcript

def extract_visual_summary(video_path, interval_sec=5):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval_sec) if fps > 0 else 1
    frames = []
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % frame_interval == 0:
            frames.append(frame)
        count += 1
    cap.release()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = YOLO("yolov8n.pt").to(device)

    labels = []
    for frame in frames:
        results = model(frame, verbose=False) 
        for r in results:
            for cls in r.boxes.cls.cpu().numpy():
                labels.append(model.names[int(cls)])

    label_counts = Counter(labels)
    top_labels = label_counts.most_common(3)
    return [label for label, _ in top_labels]

def process_video(video_path):
    transcript = extract_transcript(video_path)
    top_labels = extract_visual_summary(video_path)

    summary = "Nội dung chính: " + (", ".join(top_labels) if top_labels else "Không nhận diện được nội dung.")

    return {
        "path": video_path,
        "summary": summary,
        "transcript": transcript,
        "labels": top_labels,
        "filename": os.path.basename(video_path)
    }
