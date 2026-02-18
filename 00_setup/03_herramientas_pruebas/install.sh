#!/bin/bash

# Detect OS
OS="$(uname -s)"
echo "🖥️ Detectando sistema operativo: $OS"

if [ "$OS" = "Linux" ]; then
    # Check for Debian/Ubuntu
    if [ -f /etc/debian_version ]; then
        echo "🐧 Linux detectado. Instalando herramientas en Debian/Ubuntu..."
        sudo apt-get update
        sudo apt-get install -y curl jq
    else
        echo "⚠️ Linux detectado pero no es Debian/Ubuntu. Por favor instala 'curl' y 'jq' manualmente con tu gestor de paquetes."
        exit 1
    fi
elif [ "$OS" = "Darwin" ]; then
    echo "🍎 macOS detectado. Instalando herramientas con Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew no encontrado. Por favor instálalo primero: https://brew.sh/"
        exit 1
    fi
    brew install curl jq
else
    echo "❌ Sistema operativo no soportado automáticamente por este script ($OS)."
    echo "Por favor instala 'curl' y 'jq' manualmente."
    exit 1
fi

echo "✅ Instalación completada exitosamente."
echo "Prueba ejecutando: curl --version && jq --version"
