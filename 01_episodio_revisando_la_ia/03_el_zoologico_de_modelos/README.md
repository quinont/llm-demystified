# 03. El Zoológico de Modelos (Tamaños y Sabores)

No todas las IAs son iguales. En este capítulo vamos a correr el **mismo prompt** contra 4 cerebros radicalmente distintos para ver cómo "piensan" (o alucinan).

## 🦁 Los Tipos de Modelos

### 1. Modelos Base / Chat (General Purpose)
Son los estándar (como Llama 3, Mistral). Están entrenados para entender instrucciones y conversar. Son el "promedio" equilibrado.

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

La cuantización es convertirlo a MP3 (4 bits). Pierdes un *poquito* de calidad (inteligencia), pero el archivo pesa un tercio, corre 3 veces más rápido y lo puedes correr en una PC promedio.

---

## 🧪 El Experimento
Ejecuta `benchmark_modelos.py`. Vamos a preguntar un acertijo lógico simple:

> *"Tengo 3 camisas secándose al sol y tardan 1 hora. Si pongo 6 camisas, ¿cuánto tardan?"*

### Resultados esperados (Hipótesis):
* **Tiny:** Probablemente diga "2 horas" (falla matemática lineal).
* **Large:** Dirá "1 hora" (entiende el contexto físico).
* **Reasoning:** Te mostrará paso a paso su deducción física.
* **Uncensored:** Responderá directo y sin rodeos.

**Nota:** Como todos los modelos van a correr en el mismo servidor, la ejecución puede tomar tiempo dependiendo de tu hardware (carga/descarga de modelos en VRAM).

```bash
python benchmark_modelos.py
```

---

## Reto

Siempre es posible ir un poco más a fondo:
- ¿Qué pasa con otros modelos que conozcas?
- ¿Qué pasa si ocupas un modelo "reasoning" más pequeño? ¿O más grande?

---

## ⏭️ Siguiente Episodio

Hemos terminado la introducción básica. Sabemos hablar con la IA y sabemos que hay diferentes tipos.
Ahora, ¿qué pasa si hacemos que **dos IAs hablen entre sí**?

🔙 **[Anterior: La Verdad del Request](../02_la_verdad_del_request)** | 👉 **[Episodio 2: IA Hablando con IA](../../02_ia_hablando_con_ia)**
