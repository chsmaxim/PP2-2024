import re

with open("row.txt", "r") as file:
    content = file.read()

abstring = re.findall(r'^a.*b$', content)
print(abstring)