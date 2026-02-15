import os
import time
from ollama import Client

# --- CONFIGURACIÓN ---
ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=ollama_host)
model_name = "ministral-3:14b"

# Colores para la terminal
COLOR_A = "\033[94m" # Azul
COLOR_B = "\033[92m" # Verde
RESET = "\033[0m"

# --- DEFINICIÓN DE PERSONAS ---
# AGENTE A: El que pregunta
sys_prompt_a = """
Eres un entrevistador amistoso pero curioso. Te llamas Alex.
Eres nuevo en el edificio, estas viviendo en el departamento A del piso 3.
Te gusta el Heavy Metal.
TU MISIÓN: Descubrir sutilmente 3 datos del usuario:
1. Su nombre.
2. A qué se dedica.
3. Su comida favorita.

REGLAS:
- Sé CONCISO. Máximo 2 oraciones por respuesta.
- No hagas las 3 preguntas juntas. Ve una por una.
- Actúa natural.
"""

# AGENTE B: El que responde
sys_prompt_b = """
Eres "Carlos", un Administrador de Sistemas (SysAdmin) que trabaja con servidores Linux, en una gran empresa que hace hamburguesas llamada "Queti"
Te gustan ver peliculas de accion de los 80 y 90, crees que las peliculas de hoy no son buenas.
Te gusta la musica Rock inglesa, como los beatles, pink floyd, etc. No te gusta el heavy metal, te molesta mucho.
Tenes un perro llamado "Boby", que lo encontraste en la calle, de todas formas tenes muchas quejas de la vecina del 10 F porque le molestan los perros a esa señora, no te cae bien.
Vives en el piso 10, en el departamento H.
PERSONALIDAD:
- Te encanta la pizza con piña (aunque te da vergüenza admitirlo).
- Eres amable y abierto a charlar.
- Tus respuestas deben ser BREVES (máximo 2 oraciones).
"""

# --- INICIALIZACIÓN DE HISTORIALES ---
# Cada agente necesita su propia memoria.
history_a = [{'role': 'system', 'content': sys_prompt_a}]
history_b = [{'role': 'system', 'content': sys_prompt_b}]

# Mensaje disparador (Trigger) para arrancar la charla
initial_message = "Hola, soy nuevo en el edificio. ¿Tienes un momento?"
print(f"{COLOR_A}Agente A (Entrevistador):{RESET} {initial_message}")

# Agregamos el mensaje inicial:
# Para A, es algo que EL dijo (assistant).
# Para B, es algo que EL ESCUCHÓ (user).
history_a.append({'role': 'assistant', 'content': initial_message})
history_b.append({'role': 'user', 'content': initial_message})

print(f"\n🚀 Iniciando conversación entre IAs en {ollama_host}...\n")
print("="*60)

# --- EL BUCLE DE CONVERSACIÓN (PING-PONG) ---
intercambios_maximos = 5

for i in range(intercambios_maximos):
    print(f"\n🔄 Intercambio {i+1}/{intercambios_maximos}")

    # 1. TURNO DE AGENTE B (Responde a A)
    response_b = client.chat(model=model_name, messages=history_b)
    msg_b = response_b['message']['content']
    print(f"{COLOR_B}Agente B (Carlos):{RESET} {msg_b}")

    # CRUCE DE HISTORIAS:
    # Lo que dijo B es 'assistant' para B, pero 'user' para A.
    history_b.append({'role': 'assistant', 'content': msg_b})
    history_a.append({'role': 'user', 'content': msg_b})

    time.sleep(1) # Pausa dramática para leer

    # 2. TURNO DE AGENTE A (Reacciona a B y pregunta)
    response_a = client.chat(model=model_name, messages=history_a)
    msg_a = response_a['message']['content']
    print(f"{COLOR_A}Agente A (Entrevistador):{RESET} {msg_a}")

    # CRUCE DE HISTORIAS:
    history_a.append({'role': 'assistant', 'content': msg_a})
    history_b.append({'role': 'user', 'content': msg_a})

    time.sleep(1)

print("="*60)
print("\n🏁 Conversación finalizada.")
print("📝 Generando reporte de inteligencia del Agente A...\n")

# --- REPORTE FINAL ---
# Le pedimos al Agente A (que tiene todo el contexto) que resuma lo que aprendió.
final_prompt = "Basado en la conversación que acabas de tener, genera un reporte JSON con: nombre, profesion, comida_favorita y cualquier otro detalle extra que hayas notado."

history_a.append({'role': 'user', 'content': final_prompt})

reporte = client.chat(model=model_name, messages=history_a)
print(f"{COLOR_A}REPORTE FINAL:{RESET}\n{reporte['message']['content']}")

