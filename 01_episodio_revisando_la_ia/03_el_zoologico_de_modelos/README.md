# 03. El Zoológico de Modelos (Tamaños y Sabores)

No todas las IAs son iguales. En este capítulo vamos a correr el **mismo prompt** contra 4 cerebros radicalmente distintos para ver cómo "piensan" (o alucinan).

Obviamente estos 4 "cerebros" van a estar en el mismo host, asi que posiblemente sea muy lenta la ejecucion, ya lo veremos.

## 🦁 Los Tipos de Modelos

### 1. Modelos Base / Chat (General Purpose)
Son los estandard (como Llama 3, Mistral). Están entrenados para entender instrucciones y conversar. Son el "promedio" equilibrado.

### 2. Modelos de Razonamiento (Reasoning)
La nueva ola (como **DeepSeek-R1**). Estos modelos no responden inmediatamente; primero generan una cadena de pensamiento interna (`<think>...`) para verificar su lógica antes de hablar. Son más lentos, pero mucho mejores en matemáticas y lógica.

### 3. Modelos "Tiny" (Borde/IoT)
Modelos comprimidos (como **Qwen 0.5B** o **Llama 1B**). Están hechos para correr en celulares o Raspberry PIs. Son rápidos pero propensos a alucinar.

### 4. Modelos Sin Censura (Uncensored)
Modelos (como **Dolphin**) a los que se les ha eliminado el "Alineamiento de Seguridad". No te darán sermones morales si preguntas algo controvertido.

## ⚖️ ¿Qué es la Cuantización? (La analogía del MP3)
Verás nombres como `llama3:8b-instruct-q4_0`.
* **8b**: 8 Billones de parámetros (el tamaño del cerebro).
* **q4_0**: Cuantización a 4 bits.

Imagina que el modelo original es un audio WAV sin comprimir (FP16 - 16 bits). Pesa muchísimo, es enorme.

La cuantización es convertirlo a MP3 (4 bits). Pierdes un *poquito* de calidad (inteligencia), pero el archivo pesa un tercio y corre 3 veces más rápido, y tambien otro dato importante, lo podes correr con una PC promedio (si, en verdad es un promedio para arriba, pero no necesitas algo muy sofisticado)

---

## 🧪 El Experimento
Ejecuta `benchmark_modelos.py`. Vamos a preguntar un acertijo lógico simple:

> *"Tengo 3 camisas secándose al sol y tardan 1 hora. Si pongo 6 camisas, ¿cuánto tardan?"*

Resultados esperados:
* **Tiny:** Probablemente diga "2 horas" (falla matemática lineal).
* **Large:** Dirá "1 hora" (entiende el contexto físico).
* **Reasoning:** Te mostrará paso a paso su deducción física.
* **Uncensored:** Responderá directo y sin rodeos.

O bueno, esa es la idea antes de que comience a correr, veamos que pasa si lo ejecutamos.

NOTA: como todos los modelos van a correr en el mismo servidor, es posible que (dependiendo de tu host) el mismo tarde un tiempo en prender y apagar cada modelo, o prenda un modelo con un poco de memoria en la RAM y otro en la placa de video.

---

## Reto

Siempre es posible ir un poco mas a fondo con esto, te invito a probar:
- que pasa con otros modelos.
- Que pasa si ocupo un "reasoning" mas pequeño? o mas grande?


