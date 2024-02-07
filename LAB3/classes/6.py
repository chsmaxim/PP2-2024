def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

user_input = input(" ")
numbers = [int(x) for x in user_input.split()]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
