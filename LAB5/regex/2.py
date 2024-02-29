import re

string = input()
pattern = re.findall(r'ab{2,3}', string)

print(pattern)
