import re

string = input()
pattern = re.findall(r'a[b]*', string)

print(pattern)