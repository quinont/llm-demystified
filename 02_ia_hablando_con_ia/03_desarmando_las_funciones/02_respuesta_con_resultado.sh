#!/bin/bash

# ==========================================
# PASO 2: La Inyección del Resultado (Mock)
# ==========================================
# Simulamos que Python ejecutó la función `check_status` y devolvió:
# {"saciedad": 10, "energia": 5} (Valores críticos).
#
# El historial que enviamos ahora contiene 4 mensajes:
# 1. System
# 2. User (Pregunta original)
# 3. Assistant (La petición de tool_calls que ocurrió en el paso 1)
# 4. Tool (El resultado de la función)

echo "--- Enviando Resultado de la Tool al LLM ---"

curl http://${OLLAMA_HOST}:11434/api/chat -d '{
  "model": "ministral-3:14b",
  "stream": false,
  "messages": [
    {
      "role": "system",
      "content": "Eres un ser digital con un cuerpo simulado. TU PRIORIDAD ES TU SALUD. Si te preguntan cómo estás, SIEMPRE revisa tus constantes vitales con la herramienta."
    },
    {
      "role": "user",
      "content": "¿Cómo te sientes? ¿Tienes energía para trabajar?"
    },
    {
      "role": "assistant",
      "content": "",
      "tool_calls": [
        {
          "function": {
            "name": "check_status",
            "arguments": {}
          }
        }
      ]
    },
    {
      "role": "tool",
      "content": "{\"saciedad\": 10, \"energia\": 5, \"diagnostico\": \"CRITICO_INMINENTE\"}",
      "name": "check_status"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_status",
        "description": "Obtener los niveles actuales de hambre (saciedad) y energía.",
        "parameters": {
          "type": "object",
          "properties": {}
        }
      }
    }
  ]
}' | jq .
