encrypted = input('enter encrypted text: ')
key = 0
while True:
    try:
        decrypted = ""
        for i in range(0, len(encrypted), 4):
            decrypted += chr(int(encrypted[i:i+4], 16) ^ key)
        print(decrypted)
        key += 1
    except:
        print('error')