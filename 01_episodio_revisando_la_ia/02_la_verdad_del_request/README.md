# 02. La Verdad del Request (CURL)
En el capítulo anterior, vimos un script de Python que parecía inteligente. Ahora, vamos a ver qué estaba ocurriendo realmente en la red.


La librería ollama en Python no es más que un "envoltorio" (wrapper) que construye peticiones HTTP. No hay magia, solo texto viajando de un lado a otro.

## 📡 Anatomía de una Petición

Cuando interactúas con un LLM, no estás "abriendo un canal" de comunicación persistente. Estás enviando una carta y recibiendo una respuesta.


### El Endpoint

Todo sucede aquí: POST /api/chat

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

- model: A qué "cerebro" le estás hablando.
- messages: La parte más importante. Es una lista de objetos.
- stream: Si es true (por defecto), la IA responde palabra por palabra (efecto máquina de escribir, lo cual es la forma en la que trabaja la IA). Si es false, espera a terminar la frase para responder todo el JSON junto.

## 🧠 El Problema de la Memoria (Stateless)

Los servidores de LLM son Stateless (Sin Estado). Esto significa que no recuerdan nada entre una petición y la otra.

Si ejecutas el script 01_request_inicial.sh dos veces, la IA te responderá como si fuera la primera vez en ambas ocasiones. De todas formas, es necesario aclarar que la respuesta puede variar de una ejecucion a la otra por la forma probabilistica en la que trabaja los modelos de LLM.

### ¿Cómo funciona entonces un chat?

El "truco" es que el cliente (nosotros) debe re-enviar toda la conversación en cada turno.

- Turno 1: Envías [Mensaje A].
- Turno 2: Envías [Mensaje A, Respuesta A, Mensaje B].
- Turno 3: Envías [Mensaje A, Respuesta A, Mensaje B, Respuesta B, Mensaje C].

Si miras el archivo 02_request_con_historial.sh, verás cómo el JSON crece. Esto explica por qué los chats muy largos eventualmente se vuelven lentos o costosos: estás enviando una novela entera solo para decir "gracias".

Aca aparece algo muy interesante que es la ventana de contexto. la IA tiene una cierta cantidad de palabras (tokens) que puede llegar a conocer para poder ir generando mas palabras, este contexto puede llegar a su limite y comienza a pasar algo que vemos que el modelo de LLM comienza a "olvidarse" cosas, por lo tanto la gestion de "contexto" debe ser cuidadosa al armar una aplicacion, o podremos perder las partes mas importantes.

## 🛠️ Ejecución

Para ver la respuesta cruda de la IA:

Importante: no te olvides de cargar la variable de entorno OLLAMA_HOST con "localhost" si lo estas corriendo todo en la misma PC o la direccion IP de la pc que tiene ollama ejecutandose.

```Bash
# 1. El saludo inicial
sh 01_request_inicial.sh
```

```Bash
# 2. La respuesta con contexto acumulado
sh 02_request_con_historial.sh
```

## Reto

Aqui puedes jugar un poco mas con los script:
- Probar otros system prompt
- Eliminar algunas entradas
- Que pasa si el user escribe dos veces?
- Que pasa si el assistant escribe dos veces?

