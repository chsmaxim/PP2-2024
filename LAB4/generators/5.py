def allnumbers(n):
    for i in range(n, 0, -1):
        yield i

n = int(input("Enter number: "))

for number in allnumbers(n):
    print(number)