import math


def cal_volume_cone(r, h):
    volume = (1/3) * math.pi * math.pow(r, 2) * h
    return round(volume, 2)


radius = float(input("Enter radius(cm) of cone: "))
height = float(input("Enter height(cm) of cone: "))
volume = cal_volume_cone(radius, height)
print(f"The volume of cone is {volume:.2f} cm^3")
