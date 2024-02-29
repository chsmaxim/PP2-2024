import re

string = input()
splitupper = re.findall(r'[A-Z][^A-Z]*', string)

print(splitupper)