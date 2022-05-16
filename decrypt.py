#!/usr/bin/env/ python3
from importlib.resources import contents
import os
import sys
from pathlib import Path
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "keyfile.key" or file == "decrypt.py":
            continue
    elif os.path.isfile(file):
            files.append(file)

print (files)

with open("keyfile.key","rb") as key:
    secretkey = key.read()

secret_phrase = "worm"

user_phrase = input("Please enter the secret phrase\n")

if user_phrase == secret_phrase:
        for file in files:
                with open(file, "rb") as thefile:
                        content = thefile.read()

                contents_decrypted = Fernet(secretkey).decrypt(content)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
        print("Your files have been decrypted")
else:
        print("Incorrect Passphrase")