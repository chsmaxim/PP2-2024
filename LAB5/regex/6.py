import re

string = open("row.txt", "r")

file = string.read()

colonstring = re.sub(r'[ ,.]', ':', file)
print(colonstring)