import math


def cal_volume_cone(r, h):
    volume = (1/3) * math.pi * math.pow(r, 2) * h
    return round(volume, 2)
