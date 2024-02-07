from itertools import permutations

def get_permutations(s):
    return [''.join(p) for p in permutations(s)]

string = input(" ")
all_permutations = get_permutations(string)
print(all_permutations)
