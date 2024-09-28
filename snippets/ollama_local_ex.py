
def call_ollama_local(prompt):
    url = "http://localhost:11434/v1/completions"

    data = {
        'model': ollama_model,
        'prompt': prompt
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['text']
        else:
            return f"Local Ollama API error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Local Ollama connection error: {str(e)}"