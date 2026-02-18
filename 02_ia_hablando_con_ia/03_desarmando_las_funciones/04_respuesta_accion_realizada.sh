#!/bin/bash

# ==========================================
# PASO 4: Confirmación de la Acción
# ==========================================
# Simulamos que Python ejecutó la función con el parámetro "comer".
# Devolvemos un JSON diciendo que la saciedad subió.
#
# Historial que enviamos:
# ... (todo lo anterior) ...
# 3. Assistant: tool_calls[perform_action, args={action: comer}]
# 4. Tool: {resultado: "Comiste una pizza", nueva_saciedad: 50}

echo "--- Enviando Resultado: Ya comiste ---"

curl http://${OLLAMA_HOST}:11434/api/chat -d '{
  "model": "ministral-3:14b",
  "stream": false,
  "messages": [
    {
      "role": "system",
      "content": "Eres un ser digital. TU PRIORIDAD ES TU SALUD."
    },
    {
      "role": "user",
      "content": "¡Entonces comé algo ahora mismo!"
    },
    {
      "role": "assistant",
      "content": "",
      "tool_calls": [
        {
          "function": {
            "name": "perform_action",
            "arguments": {
              "action": "comer"
            }
          }
        }
      ]
    },
    {
      "role": "tool",
      "content": "{\"status\": \"SUCCESS\", \"mensaje\": \"Te has comido una pizza entera. Estaba deliciosa.\", \"nueva_saciedad\": 50}",
      "name": "perform_action"
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
