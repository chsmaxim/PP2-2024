import re

string = input()

sequence = re.findall(r'[a-z]+_[a-z]+', string)
print(sequence)