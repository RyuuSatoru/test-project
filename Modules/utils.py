import json
import os

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"[WARN] Không đọc được JSON từ {path}: {e}")
        return []

def is_video_file(filename):
    video_exts = [".mp4", ".mov", ".avi", ".mkv"]
    return any(filename.lower().endswith(ext) for ext in video_exts)

def is_image_file(filename):
    image_exts = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]
    return any(filename.lower().endswith(ext) for ext in image_exts)

def is_audio_file(filename):
    audio_exts = [".wav", ".mp3", ".flac", ".aac", ".ogg", ".m4a"]
    return any(filename.lower().endswith(ext) for ext in audio_exts)

def detect_keywords(text, keywords, ignore_case=True):
    if ignore_case:
        text = text.lower()
        keywords = [kw.lower() for kw in keywords]
    return any(kw in text for kw in keywords)
