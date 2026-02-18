# 🧠 Instalando Ollama

Ollama es el motor que nos permite ejecutar LLMs (Large Language Models) localmente de manera sencilla.

## 1. Instalación Oficial

Para instalar Ollama, sigue las instrucciones oficiales en su sitio web. Es la fuente más actualizada y confiable:

👉 **[Descargar Ollama](https://ollama.com/download)**

Una vez instalado, verifica que esté corriendo abriendo una terminal y ejecutando:

```bash
ollama --version
```

### ¿Por qué Ollama? (vs OpenAI, Google, Anthropic)

Aunque el código de este proyecto utiliza la librería `ollama` para interactuar con modelos locales, es importante aclarar que **los conceptos que aprenderás aquí son universales**.

La estructura de los mensajes (`system`, `user`, `assistant`), el uso de herramientas (*tool calling*), y el manejo de contexto son prácticamente idénticos si decidieras usar las APIs de:
- OpenAI (GPT-4o, o1)
- Google (Gemini)
- Anthropic (Claude)
- Groq, Mistral, etc.

**Elegimos Ollama para este curso porque:**
1.  **Es Gratis:** No necesitas tarjetas de crédito ni pagar por tokens para aprender.
2.  **Es Privado:** Tus datos no salen de tu máquina.
3.  **Es "Desmitificador":** Al correrlo en tu propia PC, ves que no es magia en la nube, es solo software ejecutándose en tu hardware.

## 2. Descargando los Modelos

Este proyecto utiliza varios modelos específicos en sus ejemplos. Necesitas descargarlos ("pull") para que los scripts de Python funcionen correctamente.

Ejecuta los siguientes comandos en tu terminal:

```bash
# Modelos base para los ejemplos
ollama pull gemma3:12b
ollama pull qwen3:14b
ollama pull dolphin3:8b
ollama pull ministral-3:14b
```

> **⚠️ Nota Importante:**
> Los nombres de los modelos (`gemma3`, `qwen3`, etc.) pueden referirse a versiones muy recientes o específicas que evolucionan rápido.
> Si alguno de los comandos falla (ej. "manifest not found"), por favor busca la versión equivalente más actual en la [librería de Ollama](https://ollama.com/library) (por ejemplo `gemma2`, `qwen2.5`, `mistral-nemo`) y actualiza la referencia en el código Python correspondiente.

## 3. Verificación Rápida

Para asegurarte de que tu instalación funciona y puedes ejecutar modelos, prueba correr un modelo pequeño (como `gemma2:2b` o el que hayas descargado):

```bash
ollama run gemma2:2b "Hola, ¿estás funcionando?"
```

Si recibes una respuesta, ¡estás listo para continuar!

---
**Navegación:**
⬅️ [Anterior (Setup Overview)](../README.md) | ➡️ [Siguiente (Entorno Python)](../02_entorno_python/README.md)
