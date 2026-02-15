import os
from ollama import Client

# 1. Configuración del Cliente
# Buscamos la variable de entorno, si no existe, usamos localhost.
ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=ollama_host)
model_name = "gemma3:12b"

# 2. El "Contexto" Inicial (System Prompt)
system_prompt = """
Eres un investigador privado astuto. Estás charlando con el usuario para sacarle información sin que se de cuenta.

Tus objetivos secretos son descubrir:
1. Su nombre.
2. A qué se dedica.
3. Su comida favorita.

REGLAS:
- NO hagas preguntas directas sobre estos datos.
- Usa la conversación casual para que el usuario los revele solo.
- Sé amigable y genera confianza.
- Se conciso.
"""

# 3. Inicialización del Historial (La "Memoria")
conversation_history = [
    {'role': 'system', 'content': system_prompt}
]

print(f"🔮 Conectado a Ollama en: {ollama_host}")
print(f"🧠 Modelo cargado: {model_name}")
print("--- El mentalista está listo. Escribe 'salir' para terminar. ---\n")

try:
    while True:
        # Capturamos entrada del usuario
        user_input = input("\033[94mTú:\033[0m ")

        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("👋 El mentalista se retira.")
            break

        # A. Agregamos el mensaje del usuario al historial
        conversation_history.append({'role': 'user', 'content': user_input})

        # B. Llamada a la API (La Abstracción)
        print("Thinking...", end="\r")
        response = client.chat(model=model_name, messages=conversation_history)

        # C. Extraemos la respuesta limpia
        ai_response = response['message']['content']

        # D. Agregamos la respuesta de la IA al historial
        conversation_history.append({'role': 'assistant', 'content': ai_response})

        print(f"\033[92mMentalista:\033[0m {ai_response}\n") # Color verde

except KeyboardInterrupt:
    print("\n👋 Sesión cerrada forzosamente.")
except Exception as e:
    print(f"\n❌ Error conectando con Ollama: {e}")
    print("Tip: Verifica que OLLAMA_HOST sea correcto y el servidor esté corriendo.")
