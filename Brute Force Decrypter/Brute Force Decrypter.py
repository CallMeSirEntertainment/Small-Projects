from time import sleep

encrypted = input('Please note that this will erase previous results.\nEnter encrypted text: ')
key = 0

while True:
    try:
        with open(__file__.replace('Brute Force Decrypter.py', 'results.txt'), 'w') as file:
            decrypted = ""
            for i in range(0, len(encrypted), 4):
                decrypted += chr(int(encrypted[i:i+4], 16) ^ key)
                key += 1
            file.write(decrypted)
    except Exception as e:
        print("Unable to decrypt.",e)
        sleep(10)
        exit()