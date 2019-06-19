def fahrenheit_to_kelvin(fahrenheit):
    """convert Fahrenheit to Kelvin

    >>> fahrenheit_to_kelvin(23)
    268.15
    >>> fahrenheit_to_kelvin(550)
    560.93
    >>> fahrenheit_to_kelvin(-250)
    116.48
    >>> fahrenheit_to_kelvin(0)
    255.37
    >>> fahrenheit_to_kelvin(57.123)
    287.11
    >>> fahrenheit_to_kelvin(-2.789542187)
    253.82

    """
    kelvin = (fahrenheit + 459.67) * (5/9)
    return round(kelvin, 2)
