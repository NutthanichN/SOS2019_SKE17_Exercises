def cal_centripetal_force(m, v, r):
    """calculate the centripetal force from given mass, velocity and radius

    >>> cal_centripetal_force(0, 0, 1)
    0.0
    >>> cal_centripetal_force(5, 10, 15)
    33.33
    >>> cal_centripetal_force(20, -5, 6)
    83.33
    >>> cal_centripetal_force(1, 1, 1)
    1.0
    >>> cal_centripetal_force(15.65, 23.87, 6.5648792)
    1358.29
    >>> cal_centripetal_force(20.73, 4.0, 16.275)
    20.38

    """
    f = (m * (v**2)) / r
    return round(f, 2)
