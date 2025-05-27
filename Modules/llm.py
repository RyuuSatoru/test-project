from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

# Tạo client với API key (bạn thay bằng API key của mình)
client = genai.Client(api_key="AIzaSyDcWAl6CxbnL0K0O4JkdffP7VMRRZZefn8")

model_id = "models/gemini-2.5-flash-preview-05-20"

google_search_tool = Tool(
    google_search=GoogleSearch()
)

config = GenerateContentConfig(
    tools=[google_search_tool],
    response_modalities=["TEXT"]
)

def query_genai(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=config
        )

        return "\n".join(part.text for part in response.candidates[0].content.parts)

    except Exception as e:
        return f"[LỖI] Không thể truy vấn Gemini: {e}"
