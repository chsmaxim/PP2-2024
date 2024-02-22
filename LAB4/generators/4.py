def generator(a, b):
    for i in range (a, b):
        yield i ** 2

a = int(input("Enter first border: "))
b = int(input("Enter second border: "))

for square in generator(a, b):
    print(square)

print(b ** 2)