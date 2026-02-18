# 🐍 Configuración del Entorno Python

Para ejecutar los scripts de este proyecto, necesitamos un entorno virtual de Python. Esto aísla nuestras dependencias del sistema global.

Se recomienda utilizar **Python 3.10, 3.11 o 3.12**.

## Instalación Rápida (Makefile)

Si tienes `make` instalado (común en Linux/Mac), simplemente ejecuta:

```bash
make install
```

Esto creará una carpeta `venv` e instalará las librerías necesarias (`ollama`, `requests`, etc.).

Por defecto, intentará usar el comando `python3`. Si deseas usar una versión específica (ej. python3.11), puedes ejecutar:

```bash
make install PYTHON_VERSION=python3.11
```

## Activación del Entorno

Una vez instalado, debes activar el entorno virtual antes de correr cualquier script:

```bash
source venv/bin/activate
```

Para salir del entorno virtual, simplemente escribe `deactivate`.

## Instalación Manual (Sin Make)

Si prefieres hacerlo manualmente o estás en Windows sin Make:

1.  Crear el entorno virtual:
    ```bash
    python3 -m venv venv
    ```
2.  Activarlo:
    - **Linux/Mac:** `source venv/bin/activate`
    - **Windows:** `venv\Scripts\activate`
3.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Siguiente paso

Ya tenemos el cerebro (Ollama) y el cuerpo (Python). Pero necesitamos gafas de rayos X para ver qué está pasando realmente en la red.

⬅️ [Volver al Paso 1: Ollama](../01_instalando_ollama/README.md) | 👉 **[Paso 3: Rayos X (Herramientas de Prueba)](../03_herramientas_pruebas/README.md)**
