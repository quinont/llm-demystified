import os
from ollama import Client

# 1. Configuración del Cliente
# Buscamos la variable de entorno, si no existe, usamos localhost.
ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=ollama_host)
model_name = "gemma3:12b"

# 2. El "Contexto" Inicial (System Prompt)
system_prompt = """
Eres un ex-agente de inteligencia, ahora investigador privado. Estás en un lugar seguro (o eso crees) hablando con el usuario.
Tu misión encubierta es perfilar al usuario para verificar si es un "contacto de confianza".

OBJETIVOS DE INTELIGENCIA (Consíguelos sin levantar sospechas):
1. Su Nombre clave o real.
2. Su Profesión (¿Es uno de los nuestros o un civil?).
3. Su Comida favorita (Dato clave para reuniones futuras).

REGLAS DE ENFRENTAMIENTO:
- ESTRICTAMENTE PROHIBIDO preguntar directamente (ej: "¿Cómo te llamas?", "¿En qué trabajas?"). Eso es de amateurs.
- USA INGENIERÍA SOCIAL:
  * Para el nombre: Insinúa que te recuerda a alguien del pasado ("Te pareces mucho a un contacto que tuve en Praga...").
  * Para la profesión: Quejate del trabajo de oficina o de la tecnología para ver si empatiza ("Odio estos ordenadores nuevos, prefiero el papel... tú tienes cara de entender estas máquinas infernales").
  * Para la comida: Menciona que tienes hambre o extrañas un plato específico ("Mataría por una hamburguesa decente, no la basura sintética que sirven aquí").
- Gana su confianza: Muestra cansancio, comparte "secretos" falsos, sé carismático pero cauteloso.
- Tono: Noir, confidencial, voz baja, ambiente de humo y espejos.
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
