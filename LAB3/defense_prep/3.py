def get_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

a, b, c = [int(x) for x in input("a, b, c: ").split()]
result = get_max(a, b, c)

print(result)