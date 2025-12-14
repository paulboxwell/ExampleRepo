import requests
import json
import os
from datetime import datetime

def query_ollama_raw(model: str, prompt: str, log_dir: str = "logs") -> dict:
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload, headers=headers)

    log_data = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "prompt": prompt,
        "raw_response": None,
        "error": None
    }

    if response.status_code == 200:
        result_text = response.json().get("response", "").strip()
        log_data["raw_response"] = result_text
    else:
        log_data["error"] = f"HTTP {response.status_code}: {response.text}"

    os.makedirs(log_dir, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_raw_log.json"
    filepath = os.path.join(log_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)

    return log_data

def main():
    print("Hello from Python inside Jenkins!")



if __name__ == "__main__":
    main()