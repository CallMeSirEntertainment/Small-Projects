import random as rand
import time
generations = 0
print("Generating...")
while True:
	number = rand.randint(0,9999999)
	generations += 1
	if number in [69, 420, 21, 69420, 42069]:
		print(f"Congrats! You got one of the special numbers after {generations} generations!\n{number} was the special number you got.\n\nGenerating...")
		time.sleep(5)