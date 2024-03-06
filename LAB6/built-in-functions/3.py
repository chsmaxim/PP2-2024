string = input()

string = ''.join(char for char in string if char.isalnum())

if string == ''.join(reversed(string)):
    print("palindrome")
else:
    print("not palindrome")