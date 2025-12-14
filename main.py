import requests
import json
from datetime import datetime

def query_ollama_raw(model: str, prompt: str) -> dict:
    url = "http://host.docker.internal:11434/api/generate"

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

    return log_data

def main():
    print("Hello from Python inside Jenkins!")

    log_data = query_ollama_raw("llama3", "What is the capital of the UK?")

    print(json.dumps(log_data, indent=2))

if __name__ == "__main__":
    main()