import re

string = input()

sequence = re.findall(r'[A-Z][a-z]+', string)
print(sequence)