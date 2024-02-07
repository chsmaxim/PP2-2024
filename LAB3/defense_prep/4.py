def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input())
result = is_even(num)

print(result)