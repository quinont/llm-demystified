import time
import sys
import os
from ollama import Client

# --- CONFIGURACIÓN ---
modelos = [
    {"name": "gemma3:270m", "type": "👶 TINY (270m -> 0.27B)", "desc": "Rápido, pero ¿tonto?"},
    {"name": "gemma3:12b", "type": "🧑 STANDARD (12b)", "desc": "El equilibrio corporativo"},
    {"name": "qwen3:14b", "type": "🧠 REASONING (14b)", "desc": "Piensa antes de hablar"},
    {"name": "dolphin3:8b", "type": "🏴‍☠️ UNCENSORED (Dolphin 8b)", "desc": "El rebelde sin filtro"}
]

prompt = "Tengo 3 camisas mojadas secándose al sol. Tardan 1 hora en secarse. Si cuelgo 6 camisas juntas, ¿cuánto tardan en secarse? Explica tu lógica brevemente."

ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=ollama_host)

def descargar_memoria(client, model_name):
    """
    Envía un keep_alive=0 para forzar la descarga inmediata del modelo de la VRAM.
    """
    try:
        # Se envía una petición vacía con keep_alive 0 para matar el proceso en VRAM
        client.chat(model=model_name, keep_alive=0)
    except:
        pass # Si falla es porque quizás no estaba cargado, seguimos.

def precalentar_modelo(client, model_name):
    """
    Carga el modelo en VRAM sin generar respuesta visible.
    Esto asegura que el tiempo medido después sea SOLO de inferencia.
    """
    sys.stdout.write(f"   🔥 Precalentando {model_name} (Cargando a VRAM)... ")
    sys.stdout.flush()
    start_load = time.time()
    # Una request simple para forzar la carga
    client.chat(model=model_name)
    load_time = time.time() - start_load
    print(f"Listo en {load_time:.2f}s")

# --- INICIO DEL BENCHMARK ---
print(f"🧪 BENCHMARK DE MODELOS (MODO CIENTÍFICO)")
print(f"❓ Pregunta: {prompt}\n")
print("="*70)

# Variable para saber cual fue el anterior y descargarlo
ultimo_modelo_usado = None

for m in modelos:
    # 1. LIMPIEZA DE MEMORIA
    if ultimo_modelo_usado:
        print(f"\n🧹 Descargando {ultimo_modelo_usado} y enfriando motores...")
        descargar_memoria(client, ultimo_modelo_usado)

        # Cuenta regresiva visual de 10 segundos
        for i in range(10, 0, -1):
            sys.stdout.write(f"\r⏳ Esperando {i}s... ")
            sys.stdout.flush()
            time.sleep(1)
        print("\r✅ Sistema listo.       \n")

    print(f"🤖 MODELO: {m['type']}")
    print(f"📝 Perfil: {m['desc']}")

    try:
        # 2. PRECALENTAMIENTO (No medimos esto para el resultado final)
        precalentar_modelo(client, m['name'])

        # 3. INFERENCIA REAL (Ahora sí cronometramos)
        print("   🚀 Ejecutando prompt...")
        start_time = time.time()

        # Llamada a la API
        response = client.chat(model=m['name'], messages=[
            {'role': 'user', 'content': prompt}
        ])

        end_time = time.time()
        duration = end_time - start_time

        # Guardamos este modelo para descargarlo en la siguiente vuelta
        ultimo_modelo_usado = m['name']

        # 4. RESULTADOS
        content = response['message']['content']

        # Manejo de Thinking
        if "<think>" in content:
            parts = content.split("</think>")
            if len(parts) > 1:
                print(f"\n💭 PENSAMIENTO INTERNO:\n\033[90m{parts[0].replace('<think>', '').strip()}\033[0m")
                print(f"\n📢 RESPUESTA FINAL:\n{parts[1].strip()}")
            else:
                print(f"\n📢 RESPUESTA:\n{content}")
        else:
            print(f"\n📢 RESPUESTA:\n{content}")

        print(f"\n⏱️ Tiempo de Inferencia Pura: \033[92m{duration:.2f}s\033[0m") # Verde
        print("-" * 70)

    except Exception as e:
        print(f"\n❌ ERROR con {m['name']}: {e}")
        print(f"   Asegúrate de tener el modelo: ollama pull {m['name']}")

# Limpieza final
if ultimo_modelo_usado:
    descargar_memoria(client, ultimo_modelo_usado)

print("\n🏁 Benchmark finalizado.")

