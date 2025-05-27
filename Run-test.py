import os
import json
import traceback
from Modules.video_processor import process_video
from Modules.image_processor import process_image
from Modules.audio_processor import process_audio
from Modules.utils import is_video_file, is_image_file, is_audio_file

MEDIA_FOLDER = "Media/"
VIDEO_JSON_PATH = "data/video.json"
IMAGE_JSON_PATH = "data/image.json"
AUDIO_JSON_PATH = "data/audio.json"

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    video_results = []
    image_results = []
    audio_results = []

    try:
        files = os.listdir(MEDIA_FOLDER)
    except Exception as e:
        print(f"[LỖI] Không thể đọc thư mục {MEDIA_FOLDER}: {e}")
        return

    print(f"[INFO] Tìm thấy {len(files)} tệp trong {MEDIA_FOLDER}")

    for filename in files:
        filepath = os.path.join(MEDIA_FOLDER, filename)

        try:
            if is_image_file(filename):
                print(f"[IMAGE] Đang xử lý {filename}...")
                result = process_image(filepath)
                result['filename'] = filename
                image_results.append(result)

            elif is_video_file(filename):
                print(f"[VIDEO] Đang xử lý {filename}...")
                result = process_video(filepath)
                result['filename'] = filename
                video_results.append(result)

            elif is_audio_file(filename):
                print(f"[AUDIO] Đang xử lý {filename}...")
                result = process_audio(filepath)
                result['filename'] = filename
                audio_results.append(result)

            else:
                print(f"[BỎ QUA] {filename} không nhận diện được loại file.")

        except Exception as e:
            print(f"[LỖI] Tệp {filename} bị lỗi:")
            traceback.print_exc()

    save_json(video_results, VIDEO_JSON_PATH)
    save_json(image_results, IMAGE_JSON_PATH)
    save_json(audio_results, AUDIO_JSON_PATH)

    print(f"\n[HOÀN TẤT] Đã lưu {len(video_results)} video, {len(image_results)} ảnh, {len(audio_results)} âm thanh.")

if __name__ == "__main__":
    main()
