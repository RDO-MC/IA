import openai

# Configura tu clave API
openai.api_key = "ingresa  aqui la api_key"

def chat_gpt(texto):
    # Define el prompt con el texto de entrada
    prompt = f"Conversación:\nUsuario: {texto}\nChatGPT:"

    # Llama a la API de OpenAI
    respuesta = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10,
    )

    # Devuelve la respuesta del modelo
    respuesta_texto = respuesta.choices[0].text.strip()
    return respuesta_texto

# Prueba la función con un ejemplo
texto_usuario = " haz tu primera pregunta "
respuesta_chat_gpt = chat_gpt(texto_usuario)
print(respuesta_chat_gpt)