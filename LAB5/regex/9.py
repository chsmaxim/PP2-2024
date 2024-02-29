import re

string = input()

result = re.sub(r'(?<=[a-z])([A-Z])', r' \1', string)
print(result)