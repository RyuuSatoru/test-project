import ipywidgets as widgets
from IPython.display import display, clear_output
from Modules.llm import query_genai
from Modules.utils import load_json

def handle_prompt(prompt):
    prompt = prompt.strip().lower()
    if prompt in ['exit', 'quit']:
        print("[INFO] Đã thoát hệ thống.")
        return

    use_video = any(kw in prompt for kw in ["video", "phim", "clip"])
    use_image = any(kw in prompt for kw in ["ảnh", "hình", "image", "photo"])
    use_audio = any(kw in prompt for kw in ["âm thanh", "audio", "tiếng", "sound", "bài hát"])

    context = ""

    if use_video:
        print("[INFO] Đang đọc video.json...")
        video_data = load_json("data/video.json")
        context += "\n".join([f"[VIDEO] {item.get('filename', 'unknown')} - {item.get('summary', '')}" for item in video_data]) + "\n"

    if use_image:
        print("[INFO] Đang đọc image.json...")
        image_data = load_json("data/image.json")
        context += "\n".join([f"[IMAGE] {item.get('filename', 'unknown')} - {item.get('summary', '')}" for item in image_data]) + "\n"

    if use_audio:
        print("[INFO] Đang đọc audio.json...")
        audio_data = load_json("data/audio.json")
        context += "\n".join([f"[AUDIO] {item.get('filename', 'unknown')} - {item.get('transcript', '')}" for item in audio_data]) + "\n"

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

# Tạo widget giao diện
text_box = widgets.Text(
    description='Prompt:',
    placeholder='Nhập prompt truy vấn...',
    layout=widgets.Layout(width='100%')
)
send_button = widgets.Button(description='Gửi')
output_area = widgets.Output()

def on_button_click(b):
    with output_area:
        clear_output()
        handle_prompt(text_box.value)

send_button.on_click(on_button_click)

display(widgets.VBox([text_box, send_button, output_area]))
