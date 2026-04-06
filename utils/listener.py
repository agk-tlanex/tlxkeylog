import os
import time
import socket
from utils import banners
from utils import printcolor

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ListenServer(dPort=4444):
    host = "0.0.0.0"
    port = dPort

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    server.settimeout(1)

    try:
        clear()
        banners.server_banner()
        time.sleep(2)
        printcolor.println("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] INICIANDO SERVIDOR", justify="left", style="bold green")
        time.sleep(2)
        printcolor.println("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] ESPERANDO CONEXIÓNES", justify="left",style="bold cyan")
        while True:
            try:
                conn, addr = server.accept()
                printcolor.println(f"[bold white][[/bold white][green]*[/green][bold white]][/bold white] CONETADO", justify="left", style="bold green")
                printcolor.printl(f"IP: {addr[0]}", style="bold cyan")
                printcolor.printl(f"ID: {addr[1]}", style="bold cyan")
                printcolor.println(f"STATUS: OPEN", style="bold cyan")

                conn.settimeout(1)

                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break

                        msg = data.decode().strip()
                        printcolor.printl(f"[bold green][{addr[0]}]>>>[/bold green] {msg}", justify="left", style="white")

                    except socket.timeout:
                        continue

                printcolor.println("\n[bold white][[/bold white][blink bold red]![/blink bold red][bold white]][/bold white] SE CERRO LA CONEXIÓN", style="bold red")
                printcolor.printl(f"IP: {addr[0]}", style="bold cyan")
                printcolor.printl(f"ID: {addr[1]}", style="bold cyan")
                printcolor.println(f"STATUS: CLOSE", style="bold cyan")
                printcolor.println("[bold white][[/bold white][green]*[/green][bold white]][/bold white] ESPERANDO CONEXIÓN", style="bold cyan")

            except socket.timeout:
                continue

    except KeyboardInterrupt:
        print("\n")
        printcolor.println("[bold white][[/bold white][blink bold yellow]-[/blink bold yellow][bold white]][/bold white] CONEXIÓN CERRADA", justify="left", style="bold yellow")


    finally:
        server.close()