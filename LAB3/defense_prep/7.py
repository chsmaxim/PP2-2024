def fibonacci(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("num: "))
result = fibonacci(num)

print(result)