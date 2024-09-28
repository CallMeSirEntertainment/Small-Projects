import pyautogui
import pyttsx3
from os import system, name
from time import sleep
#print(pyautogui.KEY_NAMES)
pyautogui.FAILSAFE = False
engine = pyttsx3.init()
def type_text(text: str, delay: float = 0.1):
    text = list(text) # type: ignore
    for char in text:
        pyautogui.press(keys=char, interval=delay)
engine.say('Who is your best friend?')
engine.runAndWait()
input('Who is your best friend?\n')
system('cls' if name == 'nt' else 'clear')
print("I don't think you heard me correctly...")
engine.say("I don't think you heard me correctly...")
engine.runAndWait()
for i in range(10):
    pyautogui.press(keys='volumeup', interval=0.25)
system('cls' if name == 'nt' else 'clear')
engine.say('Who. is. Your. Best. Friend?')
engine.runAndWait()
input('Who is your best friend?\n')
system('cls' if name == 'nt' else 'clear')
pyautogui.press('win')
type_text('I know where you are.')
pyautogui.press('win')
type_text('Where is my location?', 0.05)
sleep(5)
pyautogui.press('win')
type_text('I know every thing about you.')
pyautogui.press('win')
type_text('cmd', 1)
pyautogui.press('enter')
sleep(1.5)
type_text('systeminfo', 0.05)
pyautogui.press('enter')
sleep(2.5)
type_text('tree', 0.75)
pyautogui.press('enter')
sleep(5)
pyautogui.hotkey('alt', 'f4')
engine.say('Smile.')
engine.runAndWait()
pyautogui.press('win')
type_text('Camera', 0.05)
pyautogui.press('enter')