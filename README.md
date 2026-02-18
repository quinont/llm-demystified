# 🧙‍♂️ LLM Demystified: Quitando la Magia de la IA

Bienvenido a este viaje donde vamos a desarmar, pieza por pieza, el funcionamiento de los Modelos de Lenguaje Grande (LLMs).

El objetivo de este repositorio no es enseñarte a usar ChatGPT, sino a **entender qué pasa por debajo**. Queremos quitarle la capa de "magia" y ver los engranajes: los HTTP requests, los prompts de sistema, la gestión de memoria y cómo las IAs pueden usar herramientas.

## 🗺️ Mapa de Ruta

El contenido está dividido en "Episodios", diseñados para ser seguidos en orden. Cada carpeta contiene código funcional y explicaciones detalladas.

### 🛠️ Pre-Requisitos: `00_setup`

Antes de empezar, asegúrate de tener tu entorno listo. Revisa la carpeta `00_setup` para instalar las dependencias necesarias (Python, Ollama, etc.). **Es fundamental tener Ollama corriendo para los ejemplos.**

---

### 📺 Episodio 1: Revisando la IA
En este primer episodio, nos centraremos en los fundamentos. ¿Cómo nos comunicamos con un modelo? ¿Qué es realmente un "chat"?

- **[01. Abstracción con Python](./01_episodio_revisando_la_ia/01_abstraccion_con_python)**: Usando librerías para ocultar la complejidad.
- **[02. La Verdad del Request](./01_episodio_revisando_la_ia/02_la_verdad_del_request)**: Viendo los datos crudos que viajan por la red.
- **[03. El Zoológico de Modelos](./01_episodio_revisando_la_ia/03_el_zoologico_de_modelos)**: Probando distintos "cerebros" y sus capacidades.

👉 **[Ir al Episodio 1](./01_episodio_revisando_la_ia)**

---

### 🤖 Episodio 2: IA Hablando con IA
Una vez que entendemos lo básico, vamos a subir el nivel. ¿Qué pasa si conectamos una IA con otra? ¿Y si le damos un cuerpo?

- **[01. Conversación Simple](./02_ia_hablando_con_ia/01_conversacion_simple)**: Dos agentes autónomos charlando entre sí.
- **[02. Agentes con Estado](./02_ia_hablando_con_ia/02_agentes_con_estado)**: Dándole "necesidades biológicas" (hambre, sueño) a una IA.
- **[03. Desarmando las Funciones](./02_ia_hablando_con_ia/03_desarmando_las_funciones)**: Entendiendo el *Tool Calling* a bajo nivel.

👉 **[Ir al Episodio 2](./02_ia_hablando_con_ia)**

---

## 🚀 ¿Cómo empezar?

Simplemente ve a la carpeta del **Episodio 1** y comienza a leer. ¡Disfruta el viaje!
