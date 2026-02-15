#!/bin/bash

# PASO 1: El Primer Contacto
# Esto es exactamente lo que hizo la librería de Python en la primera línea del bucle.
# Nota el campo "stream": false. Esto es para recibir todo el JSON de respuesta del LLM de golpe
# y no token por token (que ensuciaría la terminal, y puede ser muy molesto si la respuesta es larga).

echo "--- Enviando primer mensaje al Investigador ---"

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
    }
  ],
  "stream": false
}'
