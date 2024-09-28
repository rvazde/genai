"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Quais foram os países medalistas finais das Olimpíadas de 2024?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "As Olimpíadas de 2024 ainda não aconteceram! Elas estão marcadas para acontecer em Paris, França, de 26 de julho a 11 de agosto de 2024. \n\nAssim, ainda não temos os países medalhistas finais. 😉\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Quais foram os países medalistas finais das Olimpíadas de 2024?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Como mencionei antes, as Olimpíadas de 2024 ainda não aconteceram! 😅 Elas estão marcadas para acontecer no verão de 2024, em Paris, França. \n\nAguardo ansiosamente para saber quais países serão os medalhistas finais! 🏆🏅 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Quem é o patrono da cidade de São Bernardo do Campo e qual é a sua história?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "O patrono da cidade de São Bernardo do Campo é **São Bernardo, também conhecido como São Bernardo de Claraval**. \n\n**História de São Bernardo de Claraval:**\n\n* **Vida:** Nascido em 1090 na França, Bernardo foi um monge cisterciense, teólogo e escritor. Ele fundou a Abadia de Clairvaux e se tornou um dos líderes religiosos mais influentes da sua época. \n* **Obra:**  Seu trabalho se destacou por suas reflexões sobre a vida espiritual, a busca por Deus e a vida monástica. Ele também foi um defensor fervoroso da Igreja Católica e participou ativamente de debates teológicos e políticos.\n* **Legado:** Seu legado se perpetua através de seus escritos, que influenciaram profundamente a teologia e a espiritualidade cristã, e através de sua atuação como líder religioso e reformador.\n\n**Relação com São Bernardo do Campo:**\n\n* **Origem:** A escolha de São Bernardo como patrono da cidade se deve à influência da imigração italiana, principalmente de famílias de origem lombarda, no início do século XX. \n* **Homenagem:** A cidade de São Bernardo do Campo, localizada no estado de São Paulo, Brasil, foi fundada em 1944 e recebeu o nome do santo em homenagem à região de origem dos imigrantes italianos.\n\n**A escolha de São Bernardo como patrono da cidade simboliza a fé católica, a tradição e a influência da cultura italiana na região.** \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "If we lay 5 shirts out in the sun and it takes 4 hours to dry, how long would 20\nshirts take to dry? Answer immediately giving the number and nothing else.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "4\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Q: The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. A:",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The statement is **false**. Here's why:\n\n* **Odd numbers:** 15, 5, 13, 7, 1\n* **Sum of odd numbers:** 15 + 5 + 13 + 7 + 1 = 41\n\n41 is an **odd** number. \n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)