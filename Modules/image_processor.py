# modules/image_processor.py
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load BLIP model & processor toàn cục để dùng lại
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large", use_fast=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device)

def process_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((384, 384))  # Resize chuẩn giúp model nhận ảnh rõ hơn

    inputs = processor(image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=70,
            num_beams=3,
            early_stopping=True
        )

    caption = processor.decode(output[0], skip_special_tokens=True)

    return {
        "path": image_path,
        "summary": caption
    }
