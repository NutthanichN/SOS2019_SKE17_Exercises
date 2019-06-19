"""find magnitude of an input vector"""

import math

i = float(input("Vector i: "))
j = float(input("Vector j: "))
k = float(input("Vector k: "))
magnitude_vector = math.sqrt((i**2) + (j**2) + (k**2))
print(f"From vector <{i},{j},{k}>")
print(f"The magnitude of this vector is {magnitude_vector:.2f}")