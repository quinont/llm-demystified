# 02. La Verdad del Request (CURL)

En el capítulo anterior, vimos un script de Python que parecía inteligente. Ahora, vamos a ver qué estaba ocurriendo realmente en la red.

La librería `ollama` en Python no es más que un "envoltorio" (*wrapper*) que construye peticiones HTTP. No hay magia, solo texto viajando de un lado a otro.

## 📡 Anatomía de una Petición

Cuando interactúas con un LLM, no estás "abriendo un canal" de comunicación persistente. Estás enviando una carta y recibiendo una respuesta.

### El Endpoint
Todo sucede aquí: `POST /api/chat`

### El Payload (JSON)
Esto es lo que tu script de Python construyó en segundo plano:

```JSON
{
  "model": "gemma3:12b",
  "messages": [
    { "role": "system", "content": "..." },
    { "role": "user", "content": "Hola" }
  ],
  "stream": false
}
```

- **model:** A qué "cerebro" le estás hablando.
- **messages:** La parte más importante. Es una lista de objetos.
- **stream:** Si es `true` (por defecto), la IA responde palabra por palabra (efecto máquina de escribir). Si es `false`, espera a terminar la frase para responder todo el JSON junto.

## 🧠 El Problema de la Memoria (Stateless)

Los servidores de LLM son **Stateless** (Sin Estado). Esto significa que no recuerdan nada entre una petición y la otra.

Si ejecutas el script `01_request_inicial.sh` dos veces, la IA te responderá como si fuera la primera vez en ambas ocasiones. (Aunque la respuesta puede variar ligeramente debido a la naturaleza probabilística del modelo).

### ¿Cómo funciona entonces un chat?
El "truco" es que el cliente (nosotros) debe **re-enviar toda la conversación** en cada turno.

1. **Turno 1:** Envías `[Mensaje A]`.
2. **Turno 2:** Envías `[Mensaje A, Respuesta A, Mensaje B]`.
3. **Turno 3:** Envías `[Mensaje A, Respuesta A, Mensaje B, Respuesta B, Mensaje C]`.

Si miras el archivo `02_request_con_historial.sh`, verás cómo el JSON crece. Esto explica por qué los chats muy largos eventualmente se vuelven lentos o costosos: estás enviando una novela entera solo para decir "gracias".

Aquí aparece la **Ventana de Contexto**. La IA tiene un límite de palabras (*tokens*) que puede procesar. Si superas ese límite, el modelo comienza a "olvidar" el principio de la charla.

## 🛠️ Ejecución

Para ver la respuesta cruda de la IA, ejecuta los scripts de bash.
**Importante:** No olvides configurar `OLLAMA_HOST` si no estás en localhost.

```Bash
# 1. El saludo inicial
sh 01_request_inicial.sh
```

```Bash
# 2. La respuesta con contexto acumulado
sh 02_request_con_historial.sh
```

## Reto

Aquí puedes jugar un poco más con los scripts:
- Prueba otros `system prompt`.
- Elimina algunas entradas del historial JSON.
- ¿Qué pasa si el `user` escribe dos veces seguidas?
- ¿Qué pasa si el `assistant` escribe dos veces seguidas?

---

## ⏭️ Siguiente Paso

Ya entendimos cómo hablamos con el modelo. Pero, ¿son todos los modelos iguales? Vamos a ponerlos a prueba.

🔙 **[Anterior: Abstracción con Python](../01_abstraccion_con_python)** | 👉 **[Siguiente: El Zoológico de Modelos](../03_el_zoologico_de_modelos)**
