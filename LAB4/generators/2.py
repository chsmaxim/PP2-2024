def even_generate(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter the n number: "))

generator = even_generate(n)
even = list(generator)
result = ', '.join(map(str, even))
print(result)