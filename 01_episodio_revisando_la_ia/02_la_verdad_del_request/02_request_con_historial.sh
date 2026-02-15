#!/bin/bash

# PASO 2: Simular la "Memoria"
# Como la API es "Stateless" (sin estado), si queremos seguir la charla,
# debemos enviar TODO de nuevo:
# 1. El System Prompt
# 2. El mensaje anterior del usuario
# 3. La respuesta anterior de la IA (que aquí estamos simulando/hardcodeando)
# 4. El NUEVO mensaje del usuario

echo "--- Enviando segundo mensaje (con historial inyectado) ---"

curl http://${OLLAMA_HOST}:11434/api/chat -d '{
  "model": "gemma3:12b",
  "messages": [
    {
      "role": "system",
      "content": "Eres un investigador privado astuto. Tus objetivos secretos son descubrir: 1. Su nombre. 2. A qué se dedica. 3. Su comida favorita. NO hagas preguntas directas."
    },
    {
      "role": "user",
      "content": "Hola, ¿quién eres y por qué me miras tanto?"
    },
    {
      "role": "assistant",
      "content": "Tranquilo amigo, solo observo el paisaje. Tienes cara de estar estresado... ¿mucho trabajo en la oficina hoy?"
    },
    {
      "role": "user",
      "content": "No trabajo en oficina, trabajo al aire libre."
    }
  ],
  "stream": false
}'
