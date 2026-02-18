# 📺 Episodio 1: Revisando la IA

En este primer episodio, nos enfocaremos en entender **cómo nos comunicamos con un LLM**.

A veces parece magia: escribes algo y te responden. Pero, ¿qué hay detrás de esa caja negra?

Vamos a ir pelando las capas de la cebolla:
1.  Primero, veremos la **Abstracción**: Cómo una librería de Python nos facilita la vida.
2.  Luego, veremos la **Realidad**: Qué datos viajan realmente por la red (HTTP Requests).
3.  Finalmente, veremos la **Diversidad**: Cómo diferentes modelos ("cerebros") responden de forma distinta al mismo estímulo.

---

## 📚 Capítulos

### [01. Abstracción con Python](./01_abstraccion_con_python)
Empezamos con lo fácil. Un script de Python que usa una librería para hablar con Ollama. Aquí veremos cómo se estructura una conversación básica.

### [02. La Verdad del Request](./02_la_verdad_del_request)
Quitamos la librería de Python y usamos `curl`. Veremos el JSON crudo que se envía y recibe. Entenderás por qué los modelos "olvidan" las cosas.

### [03. El Zoológico de Modelos](./03_el_zoologico_de_modelos)
Probaremos el mismo prompt en distintos modelos (Tiny, Standard, Reasoning, Uncensored) para ver cómo razonan y alucinan de formas diferentes.

---

## 🚀 ¡Comencemos!

El primer paso es ver cómo una simple librería de Python puede ocultar toda la complejidad.

👉 **[Ir al Capítulo 01: Abstracción con Python](./01_abstraccion_con_python)**
