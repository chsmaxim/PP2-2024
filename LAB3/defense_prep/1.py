def calculate_factorial(num):
    if num == 0 or num == 1:
       return 1
    return num * calculate_factorial(num - 1)

num = int(input("number:"))

result = calculate_factorial(num)
print(result)

