def create_prompt(role, task, topic, specific_question):
    # Estrutura do prompt com as tags XML
    prompt = f"""
    <prompt>
        A partir da estrutura xml abaixo:
        <role>{role}</role>
        <task>{task}</task>
        <topic>{topic}</topic>
        <specific_question>{specific_question}</specific_question>
        
        Responda a pergunta {specific_question}, usando a estrutura abaixo:
        1. Explicação básica do conceito:

        2. Analogia do cotidiano:
        
        3. Solução passo a passo da pergunta:
        
        4. Exemplo detalhado:
        
        5. Dica prática para iniciantes:
    </prompt>
    """
    return prompt.strip()