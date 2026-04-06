from rich.console import Console

def println(text, justify=None, style=None):
    console = Console()
    text = str(text)
    formated_text = text + "\n"
    console.print(formated_text, justify=justify, style=style)

def printl(text, justify=None, style=None):
    console = Console()
    text = str(text)
    formated_text = text
    console.print(formated_text, justify=justify, style=style)

