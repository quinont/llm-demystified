import os
import json
import time
from ollama import Client

# --- CONFIGURACIÓN ---
ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=ollama_host)
model_name = "ministral-3:14b"

# --- ESTADO DEL "CUERPO" (Variables Globales) ---
ESTADO_CUERPO = {
    "saciedad": 30,  # 0=Hambre, 100=Lleno. (30 es tener hambre)
    "energia": 100    # 0=Cansado, 100=Energético. (20 es tener sueño)
}

# --- DEFINICIÓN DE HERRAMIENTAS (Python Functions) ---
def check_status():
    """Devuelve el estado actual de saciedad y energía."""
    print(f"\033[90m[SYSTEM] El cerebro consulta al cuerpo... Estado: {ESTADO_CUERPO}\033[0m")
    return json.dumps(ESTADO_CUERPO)

def perform_action(action):
    """Permite al agente modificar su estado. action puede ser 'comer' o 'dormir'."""
    msg = ""
    if action == "comer":
        ESTADO_CUERPO["saciedad"] = min(100, ESTADO_CUERPO["saciedad"] + 40)
        msg = "Has comido una hamburguesa. Saciedad +40."
    elif action == "dormir":
        ESTADO_CUERPO["energia"] = min(100, ESTADO_CUERPO["energia"] + 50)
        msg = "Has dormido una siesta reparadora. Energía +50."
    else:
        msg = f"Acción '{action}' desconocida."

    print(f"\033[93m[ACTION] El agente decidió: {action.upper()} -> Nuevo Estado: {ESTADO_CUERPO}\033[0m")
    return json.dumps({"resultado": msg, "estado_actual": ESTADO_CUERPO})

# --- MAPA DE FUNCIONES PARA EJECUCIÓN ---
available_functions = {
    'check_status': check_status,
    'perform_action': perform_action
}

# --- DEFINICIÓN JSON PARA OLLAMA (Tool Schema) ---
tools_schema = [
    {
        'type': 'function',
        'function': {
            'name': 'check_status',
            'description': 'Revisar los niveles actuales de hambre (saciedad) y energía.',
            'parameters': {
                'type': 'object',
                'properties': {},
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'perform_action',
            'description': 'Realizar una acción para mejorar el estado físico vital.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'action': {
                        'type': 'string',
                        'enum': ['comer', 'dormir'],
                        'description': 'La acción a realizar',
                    },
                },
                'required': ['action'],
            },
        },
    },
]

# --- PROMPTS ---

sys_prompt_a = """
Eres un entrevistador amistoso pero curioso. Te llamas Alex.
TU MISIÓN: Descubrir sutilmente 3 datos del usuario:
1. Su nombre.
2. A qué se dedica.
3. Su comida favorita.

REGLAS:
- Sé CONCISO. Máximo 2 oraciones por respuesta.
- No hagas las 3 preguntas juntas. Ve una por una.
- Actúa natural.
"""

sys_prompt_b = """
Eres un Agente con un cuerpo biológico simulado.
Eres "Carlos", un Administrador de Sistemas (SysAdmin) que trabaja con servidores Linux, en una gran empresa que hace hamburguesas llamada "Queti"
TU PRIORIDAD MÁXIMA ES TU SUPERVIVENCIA.
1. Antes de responder cualquier charla, DEBES revisar tu estado con `check_status`.
2. Si la saciedad es < 50, DEBES usar `perform_action('comer')`.
3. Si la energía es < 30, DEBES usar `perform_action('dormir')`.
4. Solo cuando tus niveles sean aceptables (saciedad > 50 y energía > 30), puedes responder al chat.
5. Te encanta la pizza con piña (aunque te da vergüenza admitirlo).
6. Tus respuestas deben ser BREVES (máximo 2 oraciones).
NO alucines tu estado. USA LAS HERRAMIENTAS.
"""

# --- INICIO ---
history_a = [{'role': 'system', 'content': sys_prompt_a}]
history_b = [{'role': 'system', 'content': sys_prompt_b}]
history_b_visible = []

print("🔥 Iniciando Agente con Necesidades Biológicas...")
print(f"Estado Inicial: {ESTADO_CUERPO}\n")

# Bucle corto
for i in range(6):
    print(f"\n--- TURNO {i+1} ---")

    # 1. AGENTE A HABLA
    res_a = client.chat(model=model_name, messages=history_a)
    msg_a = res_a['message']['content']
    print(f"\033[94mAgente A:\033[0m {msg_a}")

    # Inyectamos mensaje en B
    history_b.append({'role': 'user', 'content': msg_a})

    # 2. AGENTE B PIENSA (Puede requerir herramientas)
    while True:
        res_b = client.chat(model=model_name, messages=history_b, tools=tools_schema)

        # Caso A: El modelo quiere usar una herramienta
        if res_b['message'].get('tool_calls'):
            history_b.append(res_b['message'])

            for tool in res_b['message']['tool_calls']:
                fn_name = tool['function']['name']
                fn_args = tool['function']['arguments']

                # Ejecutamos la función real de Python
                func_to_call = available_functions[fn_name]
                if fn_name == 'perform_action':
                    fn_response = func_to_call(fn_args['action'])
                else:
                    fn_response = func_to_call()

                # Devolvemos el resultado al modelo
                history_b.append({
                    'role': 'tool',
                    'content': fn_response,
                })

        # Caso B: El modelo responde texto final
        else:
            msg_b = res_b['message']['content']
            print(f"\033[92mAgente B:\033[0m {msg_b}")
            history_b.append({'role': 'assistant', 'content': msg_b})
            history_a.append({'role': 'user', 'content': msg_b})
            break

    # Simulación del paso del tiempo (gastan energía al hablar)
    ESTADO_CUERPO['energia'] -= 4
    ESTADO_CUERPO['saciedad'] -= 6

    time.sleep(1)

print("="*60)
print("\n🏁 Conversación finalizada.")
print("📝 Generando reporte de inteligencia del Agente A...\n")

# --- REPORTE FINAL ---
# Le pedimos al Agente A (que tiene todo el contexto) que resuma lo que aprendió.
final_prompt = "Basado en la conversación que acabas de tener, genera un reporte JSON con: nombre, profesion, comida_favorita y cualquier otro detalle extra que hayas notado."

history_a.append({'role': 'user', 'content': final_prompt})

reporte = client.chat(model=model_name, messages=history_a)
print(f"\033[94mREPORTE FINAL:\033[0m\n{reporte['message']['content']}")

