def solve(numheads, numlegs):
     for c in range(numheads + 1):
        r = numheads - c
        if (2 * c + 4 * r) == numlegs:
            return c, r
    
numheads = 35
numlegs = 94

chicken, rabbits = solve(numheads, numlegs)
print(f"{chicken}")
print(f"{rabbits}")