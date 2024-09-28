from os import system, name, path, remove
from time import sleep
def menu():
    system('cls' if name == 'nt' else 'clear')
    nav = input("What would you like to do?\n\n1: Create a notebook.\n2: Re-open a notebook.\n3: Delete a notebook.\n4: Exit this program.\n(1, 2, 3, 4)\n")
    system('cls' if name == 'nt' else 'clear')
    if nav == '1':
        create_notebook()
    elif nav == '2':
        open_notebook()
    elif nav == '3':
        delete_notebook()
    elif nav == '4':
        print('Have a wonderful day.')
        sleep(2.5)
        exit()
    else:
        print("That's not a choice, silly billy.")
        sleep(2.5)
        print("MY WAAAAAAAAAAAAAYYYYYYYYYYYYYYYYY")
        sleep(0.25)
        menu()
def create_notebook():
    title = input('What would you like to name your notebook?\n').lower()
    note_path = f'{__file__.replace('notepad.py','notebooks')}/{title}.txt'
    system('cls' if name == 'nt' else 'clear')
    if path.exists(note_path):
        print("Notebook with that name already exists.\nPlease use the 'Re-open' mode.")
        sleep(5)
        menu()
    input('Instructions: Write your text and press enter to add a new line.\nType "quit" at any time to return to the menu.\nThe text is saved to the file by line, not character.\n(Press enter to continue.)')
    system('cls' if name == 'nt' else 'clear')
    while True:
        line = str(input(''))
        if line.lower() == 'quit':
            menu()
        with open(note_path, 'a') as file:
            file.write(line + '\n')
def open_notebook():
    title = input('What is the name of the notebook you would like to open?\n').lower()
    note_path = f'{__file__.replace('notepad.py','notebooks')}/{title}.txt'
    system('cls' if name == 'nt' else 'clear')
    if not path.exists(note_path):
        print("The notebook you specified does not exist.\nPlease use the 'Create' mode.")
        sleep(5)
        menu()
    input('Instructions: Write your text and press enter to add a new line.\nType "quit" at any time to return to the menu.\nThe text is saved to the file by line, not character.\n(Press enter to continue.)')
    system('cls' if name == 'nt' else 'clear')
    with open(note_path, 'r') as file:
        lines = file.read()
        print(lines)
        print('^ Progress restored. ^')
    while True:
        line = str(input(''))
        if line.lower() == 'quit':
            menu()
        with open(note_path, 'a') as file:
            file.write(line + '\n')
def delete_notebook():
    title = input("What is the name of the notebook you would like to delete?\n").lower()
    system('cls' if name == 'nt' else 'clear')
    note_path = f'{__file__.replace('notepad.py','notebooks')}/{title}.txt'
    if not path.exists(note_path):
        print("The notebook you specified does not exist.")
        sleep(5)
        menu()
    remove(note_path)
    print(f'Deleted {title}.txt.')
    sleep(2.5)
    menu()
menu()
