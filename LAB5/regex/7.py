import re

snakestr = input()
wordsinsnake = snakestr.split('_')

camelstr = wordsinsnake[0] + ''.join(word.capitalize() for word in wordsinsnake[1:])
print(camelstr)