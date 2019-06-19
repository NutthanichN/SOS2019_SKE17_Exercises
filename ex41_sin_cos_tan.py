"""calculate sin, cos and tan

test cases
    >>> degree = 30
    From an angle 30.00 degrees
    sin(30.00) = 0.50
    cos(30.00) = 0.87
    tan(30.00) = 0.58
    >>> degree = 90
    From an angle 90.00 degrees
    sin(90.00) = 1.00
    cos(90.00) = 0.00
    tan(90.00) = 16331239353195370.00
    >>> degree = 125
    From an angle 125.00 degrees
    sin(125.00) = 0.82
    cos(125.00) = -0.57
    tan(125.00) = -1.43
    >>> degree = 180
    From an angle 180.00 degrees
    sin(180.00) = 0.00
    cos(180.00) = -1.00
    tan(180.00) = -0.00
    >>> degree = 230.625
    From an angle 230.62 degrees
    sin(230.62) = -0.77
    cos(230.62) = -0.63
    tan(230.62) = 1.22
    >>> degree = 270
    From an angle 270.00 degrees
    sin(270.00) = -1.00
    cos(270.00) = -0.00
    tan(270.00) = 5443746451065123.00
    >>> degree = 300
    From an angle 300.00 degrees
    sin(300.00) = -0.87
    cos(300.00) = 0.50
    tan(300.00) = -1.73
    >>> degree = 360
    From an angle 360.00 degrees
    sin(360.00) = -0.00
    cos(360.00) = 1.00
    tan(360.00) = -0.00
    >>> degree = 0
    From an angle 0.00 degrees
    sin(0.00) = 0.00
    cos(0.00) = 1.00
    tan(0.00) = 0.00
    >>> degree = -30
    From an angle -30.00 degrees
    sin(-30.00) = -0.50
    cos(-30.00) = 0.87
    tan(-30.00) = -0.58
"""

import math

degree = float(input("Enter an angle(degrees): "))
radian = math.radians(degree)
sin = math.sin(radian)
cos = math.cos(radian)
tan = math.tan(radian)
print(f"From an angle {degree:.2f} degrees")
print(f"sin({degree:.2f}) = {sin:.2f}")
print(f"cos({degree:.2f}) = {cos:.2f}")
print(f"tan({degree:.2f}) = {tan:.2f}")