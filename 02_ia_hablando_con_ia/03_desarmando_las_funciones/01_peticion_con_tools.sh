#!/bin/bash

# ==========================================
# PASO 1: El "Handshake" (Petición Inicial)
# ==========================================
# Aquí le decimos al modelo:
# 1. Quién es (System Prompt con necesidades biológicas).
# 2. Qué herramientas tiene disponibles (check_status).
# 3. La pregunta del usuario.

echo "--- Enviando Petición Inicial (Prompt + Tools) ---"

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
