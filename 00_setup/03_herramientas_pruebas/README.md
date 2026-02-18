# 🧰 Herramientas de Prueba

Para analizar las respuestas de la IA (que suelen venir en JSON) y para hacer peticiones manuales a la API de Ollama, utilizaremos dos herramientas fundamentales de línea de comandos:

1.  **`curl`**: Para hacer peticiones HTTP desde la terminal.
2.  **`jq`**: Para procesar y colorear la salida JSON, haciéndola legible.

## Instalación Automática (Linux/Mac)

Hemos incluido un script para facilitar la instalación en sistemas basados en Debian/Ubuntu y macOS.

1.  Dale permisos de ejecución al script:
    ```bash
    chmod +x install.sh
    ```
2.  Ejecútalo:
    ```bash
    ./install.sh
    ```

## Instalación Manual

Si el script no funciona o prefieres hacerlo tú mismo:

### Ubuntu / Debian
```bash
sudo apt-get update
sudo apt-get install -y curl jq
```

### macOS (Homebrew)
```bash
brew install curl jq
```

### Windows
Para Windows, se recomienda usar **WSL2** (Windows Subsystem for Linux) y seguir las instrucciones de Ubuntu.
Alternativamente, puedes instalar `curl` y `jq` con `winget` o Chocolatey, pero su uso en PowerShell puede variar ligeramente.

---
**Navegación:**
⬅️ [Anterior (Entorno Python)](../02_entorno_python/README.md) | 🚀 [**¡Comenzar Episodio 1!**](../../01_episodio_revisando_la_ia/README.md)
