import os
import json
import google.generativeai as genai


GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def create_prompt(role, task, topic, specific_question):
    prompt = f"""
        <role>{role}</role>
        <topic>{topic}</topic>
        <task>{task}</task>
        <note>Se possível, gere sua resposta com quebra de linha entre cada componente, seguindo o <document_template> ... </document_template>
        <specific_question>{specific_question}</specific_question>
        <document_template>
        Gere sua resposta formatada da seguinte maneira:

        ## specific_question

        ### 1. Explicação básica do conceito:

        [preencha_aqui]

        ### 2. Analogia do cotidiano:

        [preencha_aqui]

        ### 3. Solução passo a passo da pergunta:

        * ** [preencha_aqui]
        * ** [preencha_aqui]
        * ** [preencha_aqui]

        ### 4. Exemplo detalhado:

        [preencha_aqui]

        **Exemplo:**
        1. **Dúvida** [preencha_aqui]
        2. **Dúvida ainda maior:** [preencha_aqui]
        3. **Certeza:** [preencha_aqui]
        4. **Conclusão:** [preencha_aqui]

        ### 5. Dica prática para iniciantes:

        [preencha_aqui]
        <document_template>
    """
    return prompt.strip()

def send_to_gemini(prompt):
    return __consult_gemini(prompt)
    

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
    #print(json.dumps(json.loads(response.text), indent=4))

    return response.text


def main():
    role = "especialista em filosofia e história da ciência"
    task = "explicar o pensamento de Descartes e sua influência para iniciantes em filosofia"
    topic = "René Descartes e o Método Cartesiano"
    specific_question = "Quem foi René Descartes e qual é o significado da frase 'Penso, logo existo'?"
    prompt = create_prompt(role, task, topic, specific_question)
    response = send_to_gemini(prompt)
    print("\nResposta do Gemini 1.5 Flash:")
    print(response)

if __name__ == "__main__":
    main()
