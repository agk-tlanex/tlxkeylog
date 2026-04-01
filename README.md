# TlxKeyLogger

Un keylogger remoto desarrollado en Python con capacidad de transmisión en tiempo real y compilación a ejecutable.

## 🚀 Características

- ✅ Captura de teclas en tiempo real
- ✅ Transmisión de datos por red TCP
- ✅ Soporte completo para caracteres UTF-8 (ñ, á, é, í, ó, ú, etc.)
- ✅ Detección de combinaciones de teclas (Ctrl+C, Ctrl+V, Alt+Tab, etc.)
- ✅ Compilación a archivo .exe para Windows
- ✅ Interfaz de usuario interactiva con colores
- ✅ Registro de logs en formato texto y JSON
- ✅ Soporte para conexión remota via Ngrok

## 📋 Requisitos

- Python 3.7+
- pynput
- colorama (para la interfaz de colores)

## 🛠️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/agk-tlanex/tlxkeylogger.git
cd tlxkeylogger

# Instalar dependencias
pip install -r requirements.txt
