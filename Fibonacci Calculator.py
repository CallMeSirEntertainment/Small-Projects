from os import system
from sys import set_int_max_str_digits

set_int_max_str_digits(0)

def clear():
    system('clear')

def fib_generator(n: int):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b

def main():
    clear()
    try:
        number = int(input('What Fibonacci number would you like to calculate?\n'))
        if number < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    clear()
    save_to_file_choice = input('Would you like to save the result to a file? (y/n)\n').lower()
    save_to_file = save_to_file_choice == 'y'
    save_steps = False
    if save_to_file:
        clear()
        save_steps_choice = input("Would you like to save each step to the file? (y/n)\n").lower()
        save_steps = save_steps_choice == 'y'
    clear()
    print('Calculating, this may take a while...')
    if save_to_file:
        file_name = 'fibonacci-result.txt'
        try:
            with open(file_name, 'w') as file:
                clear()
                print(f"Saving result to {file_name}...\nDo not close this program or open the file.")
                if save_steps:
                    file.write('The final result is at the bottom of the file.\n\n')
                    final_num = 0
                    for i, num in enumerate(fib_generator(number)):
                        file.write(f'Number {i} in the Fibonacci sequence is:\n{num}.\n\n')
                        final_num = num
                    file.write(f'Final result:\n{final_num}.')
                else:
                    final_num = 0
                    for num in fib_generator(number):
                        final_num = num
                    file.write(f'Number {number} in the Fibonacci sequence is:\n{final_num}.')
            clear()
            print(f'Result saved to {file_name}.')
        except IOError as e:
            clear()
            print(f"Error saving file: {e}")
    else:
        final_num = 0
        for num in fib_generator(number):
            final_num = num
        clear()
        print(f'Number {number} in the Fibonacci sequence is:\n{final_num}.')

if __name__ == '__main__':
    main()
