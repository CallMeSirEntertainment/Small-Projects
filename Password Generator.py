import string
import random
def generate_password():
    length = 0
    while length < 5 or length > 100:
        length = int(input("Enter the desired length of the password: "))
        if length < 5:
            print("Password length should be at least 5. Please try again.")
        elif length > 100:
            print("Warning: It is not advised to generate a password greater than 100 characters.")
            proceed = input("Proceed anyway? (y/n): ")
            if proceed.lower() != "y":
                length = 0
            else:
                break
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    all_character_sets = [lowercase, uppercase, digits, punctuation]
    password = []
    for character_set in all_character_sets:
        password.extend(random.sample(character_set, 1))
    all_characters = ''.join(all_character_sets)
    for i in range(length - len(password)):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    password = ''.join(password)
    return password
while True:
    print(f'{generate_password()}\nPlease save this password. It will not be shown again.')
    if input("Do you want to generate another password? (y/n): ").lower() != "y":
        break