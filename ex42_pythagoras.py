"""find the longest side of the triangle"""

import math

side_a = int(input("The length of side a: "))
side_b = int(input("The length of side b: "))
if side_a <= 0 or side_b <= 0:
    print("Side a and side b must be greater than 0")
else:
    side_c = math.sqrt((side_a**2) + (side_b**2))
    print(f"The longest side is {side_c:.3f}")
