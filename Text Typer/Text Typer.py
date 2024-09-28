from pyautogui import write
import time
time.sleep(10)
with open(f"{__file__.replace('Text Typer.py', 'text.txt')}") as file:
    text = file.read()
for char in text:
    write(char)
