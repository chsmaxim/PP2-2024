def generate_square(N):
    for i in range(N):
        yield i ** 2

N = int(input("Some number: "))

for square in generate_square(N):
    print(square)
