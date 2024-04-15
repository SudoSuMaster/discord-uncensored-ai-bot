import requests
from random import choice, randint

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

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'What color is angel' in lowered:
        return 'black'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif '!ask' in lowered:
        if len(user_input) <= len('!ask'):  # Check if the input is only '!ask' without any additional text
            return "Please provide a prompt after '!ask'"
        else:
            prompt = user_input[len('!ask') + 1:]  # Extract the prompt after '!ask '
            fixed_text = fix_text(prompt)
            if fixed_text:
                return fixed_text
            else:
                return "useless error code"

