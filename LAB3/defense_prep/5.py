def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]

innumbers = input(" ")
list = [int(num) for num in innumbers.split()]

result = filter_primes(list)
print(result)

