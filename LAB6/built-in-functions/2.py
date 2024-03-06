string1 = input("Enter the string to calculate: ")

numberofupper = 0
numberoflower = 0

for char in string1:
    if 65 <= ord(char) <= 90:
        numberofupper += 1 
    elif 97 <= ord(char) <= 122:
        numberoflower += 1 

print(f"number of upper case letters: {numberofupper}")
print(f"number of lower case letters: {numberoflower}")