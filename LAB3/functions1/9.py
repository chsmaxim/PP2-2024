import math

def spherevolume(radius):
    volume = (4 * math.pi * pow(radius, 3)) / 3
    return volume

radius = float(input(" "))
print(spherevolume(radius))