#ceasar cipher

from rsa import encrypt

number1 = str(input("What do you what to encrypt: "))
number2 = int(input("key: "))
#selection of key and word that want to be encrypted

def caesarCipher(string, key):
    encrypt_string = []
    new_key = key % 26
    for letter in string:
        encrypt_string.append(getNewLetter(letter, new_key))

    return ''.join(encrypt_string)


def getNewLetter(letter, key):
    new_letter = ord(letter) + key
    return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter%122)
    #ceasar cipher algorithm

print(caesarCipher(number1, number2))
#results