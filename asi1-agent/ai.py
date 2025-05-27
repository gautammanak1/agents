import json
import os

import requests

ASI1_URL = "https://api.asi1.ai/v1/chat/completions"
MODEL_ENGINE = os.getenv("MODEL_ENGINE", "asi1-mini")
ASI1_API_KEY = os.getenv("OPENAI_API_KEY", "")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ASI1_API_KEY}",
}



# Send a prompt and context to the AI model and return the content of the completion
def get_completion(context: str, prompt: str, max_tokens: int = MAX_TOKENS) -> str:
    data = {
        "model": MODEL_ENGINE,
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
    }

    try:
        response = requests.post(
            ASI1_URL, headers=HEADERS, data=json.dumps(data), timeout=120
        )
    except requests.exceptions.Timeout:
        return "The request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

    messages = response.json()["choices"]
    message = messages[0]["message"]["content"]

    return message
