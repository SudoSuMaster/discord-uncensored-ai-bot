import time
import httpx
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "llama2-uncensored:latest",
    "keep_alive": "5m",
    "stream": False,
}

def fix_text(prompt):
    response = httpx.post(
        OLLAMA_ENDPOINT,
        json={"prompt": prompt, **OLLAMA_CONFIG},
        headers={"Content-Type": "application/json"},
        timeout=1000,
    )
    if response.status_code != 200:
        print("Error", response.status_code)
        return None
    return response.json()["response"].strip()
#string for prompt
text = 'what is 1+1?'

def main():    
        prompt = (
            text
        )
        fixed_text = fix_text(prompt)
        if fixed_text:
            print("Prompt:")
            print(fixed_text)
        else:
            print("Failed to fix the text. Please try again.")

if __name__ == "__main__":
    main()
