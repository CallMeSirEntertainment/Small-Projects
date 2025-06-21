from functools import cache
from os import system, name
import gc
from sys import set_int_max_str_digits
set_int_max_str_digits(0)
steps = []
save_steps = False
@cache
def fib(n: int) -> int:
    gc.collect()
    if n <=1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
number = int(input('What fibonacci number would you like to calculate?\nWarning: Large calculations use a bunch of RAM and may stall your PC.\n'))
system('cls' if name == 'nt' else 'clear')
save_to_file = input('Would you like to save the result to a file? (y/n)\n').lower()
if save_to_file == 'y':
    system('cls' if name == 'nt' else 'clear')
    save_steps = input("Would you like to save each step to the file? (y/n)\nNot recommended for calculations greater than 100000.\n").lower()
system('cls' if name == 'nt' else 'clear')
print('Calculating, this may take a while...')
for i in range(0,number + 1):
    num = fib(i)
    if save_steps == 'y':
        steps.append(num)
if save_to_file == 'y':
    with open('fibonacci-result.txt', 'w') as file:
        system('cls' if name == 'nt' else 'clear')
        print("Saving result to fibonacci-result.txt...\nDo not close this program or open the file.")
        if save_steps == 'y':
            file.write('The final result is at the bottom of the file.\n\n')
            for i in range(len(steps) - 1):
                step = steps[i]
                file.write(str(f'Number {i} in the fibonacci sequence is:\n{str(step)}.\n\n'))
            file.write(str(f'Final result:\n{str(fib(number))}.'))
        else:
            file.write(str(f'Number {number} in the fibonacci sequence is:\n{str(fib(number))}.'))
    system('cls' if name == 'nt' else 'clear')
    print(f'Result saved to fibonacci-result (ID {id}).txt.')
else:
    system('cls' if name == 'nt' else 'clear')
    print(f'Number {number} in the fibonacci sequence is:\n{fib(number)}.')