import os
import ollama
from groq import Groq
import google.generativeai as genai

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


def format_prompt(prompt):
    formatted_prompt = f"""
        <role>Assistant specialized in parsing Job Descriptions and outputting relevant structured data</role>
        <topic>Job Description from LinkedIn</topic>
        <structure_fields>
            **Name of role:** [fill_here]

            **Working hours:** [fill_here]

            **Country:** [fill_here]

            **Tech Skills:** [fill_here]

            **Salary:** [fill_here]
        </structure_fields>
        <job_description>{prompt}</job_description>
        <task>Parse <job_description> and extract relevant data, and output it structured by <structure_fields> pattern. If cannot find structure data, just add 'N/A' to field</task>
    """
    return formatted_prompt.strip()


def query_all_models(prompt):
    print('Consultando Gemini...')
    gemini_response = __consult_gemini(prompt)

    print('Consultando Groq...')
    groq_response = __consult_groq(prompt)

    print('Consultando Ollama...')
    ollama_response = __consult_ollama(prompt)

    return {
        "Gemini 1.5 Flash": gemini_response,
        "Groq llama3-8b-8192": groq_response,
        "Ollama qwen2:1.5b": ollama_resBased on the provided job description, I will now extract the relevant data and output it in the specified structure fields.

**Name of role:** Research Engineer, Language - Generative AI

**Working hours:** N/A

**Country:** Not specified (assumed to be the United States, as it does not explicitly state a specific country)

**Tech Skills:** Python, PyTorch, machine learning, deep learning, natural language processing

**Salary:** N/A (not explponse
    }


def __consult_gemini(prompt):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat()
    response = chat_session.send_message(prompt)

    return response.text


def __consult_groq(prompt):
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


def __consult_ollama(prompt):
    response = ollama.chat(
        model="qwen2:1.5b",
        messages = [
            {
                "role": "user",
                "content": prompt
            },
        ])
    return response["message"]["content"]


def main():
    with open("job_description.txt", "r") as file:
        job_description = file.read()
    formatted_prompt = format_prompt(job_description)
    results = query_all_models(formatted_prompt)
    for model, response in results.items():
        print(f"\nAnálise do {model}:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()
