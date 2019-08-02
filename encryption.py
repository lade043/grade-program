from Crypto.Cipher import AES
import random
import string


def encrypt(password, text):
    random.seed(password)
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(32))
    add = 16 - (len(text) % 16)
    for i in range(add):
        text += " "
    chiffre = AES.new(password, AES.MODE_ECB)
    chiffrat = chiffre.encrypt(text)
    return chiffrat


def decrypt(password, chiffrat):
    random.seed(password)
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(32))
    chiffre = AES.new(password, AES.MODE_ECB)
    text = chiffre.decrypt(chiffrat)
    temp_text = text.decode('ascii')
    for counter, letter in enumerate(reversed(text.decode('ascii'))):
        if letter == " ":
            temp_text = temp_text[:-1]
        else:
            break
    text = temp_text
    return text
