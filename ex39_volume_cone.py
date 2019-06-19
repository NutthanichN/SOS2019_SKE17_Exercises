import math


def cal_volume_cone(r, h):
    """calculate a volume of ellipse

    >>> cal_volume_cone(7, 12)
    615.75
    >>> cal_volume_cone(15.9, 20.214)
    5351.5
    >>> cal_volume_cone(189.56423, 1)
    37630.62
    >>> cal_volume_cone(0, 1)
    0.0
    >>> cal_volume_cone(1, 1)
    1.05
    >>> cal_volume_cone(-1, -1)
    -1.05

    """
    volume = (1/3) * math.pi * math.pow(r, 2) * h
    return round(volume, 2)
