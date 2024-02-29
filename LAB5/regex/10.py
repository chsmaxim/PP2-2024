import re

camelstr = input()

snakestr = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camelstr).lower()
print(snakestr)