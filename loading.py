from time import sleep
from os import system, name

loading_sequence = ["|","/","--","\\","|","/","--","\\"]

def loading(loops, loading_message, completion_message) -> None:
    for i in range(loops):
        system('cls' if name == 'nt' else 'clear')
        for symbol in loading_sequence:
            print(f"{loading_message}... {symbol}")
            sleep(0.75)
            system('cls' if name == 'nt' else 'clear')
    confirm = input(f"{completion_message} Press enter to continue.")
        
def loading_indicator(loading_message, completion_message) -> None:
    system('cls' if name == 'nt' else 'clear')
    for symbol in loading_sequence:
        print(f"{loading_message}... {symbol}")
        sleep(0.75)
        system('cls' if name == 'nt' else 'clear')
    confirm = input(f"{completion_message} Press enter to continue.")