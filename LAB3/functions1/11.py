def is_palindrome(input_str):
    clean_str = ''.join(input_str.lower().split())

    return clean_str == clean_str[::-1]


word = input("word: ")
result = is_palindrome(word)

if result:
    print(f"palindrome")
else:
    print(f"not palindrome")
