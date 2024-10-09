import os

API_CONFIG = {
    "base_url": "http://127.0.0.1:8000",
    "api_key": None  
}

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")


def get_api_headers():
    headers = {
        "Content-Type": "application/json"
    }

    if API_CONFIG['api_key']:
        headers["Authorization"] = f"Bearer {API_CONFIG['api_key']}"
    
    return headers


