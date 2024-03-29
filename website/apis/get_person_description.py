from dotenv import load_dotenv
from PIL import Image
import base64
import requests
import os
import io

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MAX_IMG_SIZE = 512
MAX_TOKEN_RESPONSE = 128
PROMPT = """
describe the physical characters of this person, 
keep it super brief, just bullet point description,
include race, hair color, eye color, clothing, recognizable features,
height, build, etc
"""


def encode_image(image_path: str) -> str:
    image = Image.open(image_path)
    width, height = image.size
    image = image.resize((min(width, MAX_IMG_SIZE), min(height, MAX_IMG_SIZE)))

    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    data = buffer.getvalue()

    base64_image = base64.b64encode(data).decode("utf-8")
    return base64_image


def get_person_description(image_path: str) -> str:
    try:
        base64_image = encode_image(image_path)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            "max_tokens": MAX_TOKEN_RESPONSE,
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
        )

        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return ""


def main() -> None:
    print(get_person_description("dataset/initial_image.png"))


if __name__ == "__main__":
    main()
