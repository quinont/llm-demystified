#!/bin/bash

# ==========================================
# PASO 3: Forzando la Acción (Argumentos)
# ==========================================
# Situación: El agente YA SABE que tiene hambre (Saciedad: 10).
# El usuario le dice: "¡Comé algo urgente!"
#
# Esperamos que el LLM llame a 'perform_action' con el argumento 'comer'.

echo "--- Enviando Petición: ¡Comé algo! ---"

curl http://${OLLAMA_HOST}:11434/api/chat -d '{
  "model": "ministral-3:14b",
  "stream": false,
  "messages": [
    {
      "role": "system",
      "content": "Eres un ser digital. TU PRIORIDAD ES TU SALUD. Si tienes hambre, USA LA HERRAMIENTA para comer."
    },
    {
      "role": "user",
      "content": "¿Cómo estás?"
    },
    {
      "role": "assistant",
      "content": "Me siento muy débil. Mi nivel de saciedad es crítico (10/100)."
    },
    {
      "role": "user",
      "content": "¡Entonces comé algo ahora mismo!"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "perform_action",
        "description": "Realizar una acción vital para recuperar estado.",
        "parameters": {
          "type": "object",
          "properties": {
            "action": {
              "type": "string",
              "enum": ["comer", "dormir"],
              "description": "La acción a realizar."
            }
          },
          "required": ["action"]
        }
      }
    }
  ]
}' | jq .
