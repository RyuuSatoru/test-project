from Modules.llm import query_genai
from Modules.utils import load_json, detect_keywords

try:
    from IPython.display import display, clear_output
    import ipywidgets as widgets
    COLAB = True
except ImportError:
    COLAB = False

def get_input_colab():
    text_input = widgets.Text(
        value='',
        placeholder='Nhập prompt truy vấn...',
        description='Prompt:',
        disabled=False
    )
    display(text_input)

    done_button = widgets.Button(description="Gửi")
    output = widgets.Output()
    display(done_button, output)

    user_input = {"value": ""}

    def on_button_clicked(b):
        user_input["value"] = text_input.value.strip()
        with output:
            clear_output()
            print(f">> {user_input['value']}")

    done_button.on_click(on_button_clicked)

    while not user_input["value"]:
        pass
    return user_input["value"].lower()


def main():
    print("=== HỆ THỐNG TRỢ LÝ TRUY VẤN ĐA PHƯƠNG TIỆN ===")

    while True:
        prompt = get_input_colab() if COLAB else input(">> ").strip().lower()

        if prompt in ['exit', 'quit']:
            print("[INFO] Đã thoát hệ thống.")
            break

        # Phân tích prompt để chọn nguồn dữ liệu
        use_video = any(kw in prompt for kw in ["video", "phim", "clip"])
        use_image = any(kw in prompt for kw in ["ảnh", "hình", "image", "photo"])
        use_audio = any(kw in prompt for kw in ["âm thanh", "audio", "tiếng", "sound", "bài hát"])

        context = ""

        if use_video:
            print("[INFO] Đang đọc video.json...")
            video_data = load_json("data/video.json")
            context += "\n".join([
                f"[VIDEO] {item.get('filename', 'unknown')} - {item.get('summary', '')}"
                for item in video_data
            ]) + "\n"

        if use_image:
            print("[INFO] Đang đọc image.json...")
            image_data = load_json("data/image.json")
            context += "\n".join([
                f"[IMAGE] {item.get('filename', 'unknown')} - {item.get('summary', '')}"
                for item in image_data
            ]) + "\n"

        if use_audio:
            print("[INFO] Đang đọc audio.json...")
            audio_data = load_json("data/audio.json")
            context += "\n".join([
                f"[AUDIO] {item.get('filename', 'unknown')} - {item.get('transcript', '')}"
                for item in audio_data
            ]) + "\n"

        if not (use_video or use_image or use_audio):
            print("[INFO] Đang đọc document.json...")
            doc_data = load_json("data/document.json")
            context += "\n".join(doc_data)

        full_prompt = f"{prompt}\n\nThông tin liên quan:\n{context}"

        print("[INFO] Đang gửi truy vấn...")
        response = query_genai(full_prompt)

        print("\n=== KẾT QUẢ PHẢN HỒI ===")
        print(response)
        print("\n------------------------\n")

if __name__ == "__main__":
    main()
