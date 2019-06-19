def centimeters_to_inches(cm):
    """convert centimeters to inches

    >>> centimeters_to_inches(10)
    3.937
    >>> centimeters_to_inches(2.5964)
    1.022
    >>> centimeters_to_inches(1.597815498)
    0.629
    >>> centimeters_to_inches(0)
    0.0
    >>> centimeters_to_inches(-64)
    -25.197
    >>> centimeters_to_inches(36)
    14.173
    """
    inch = cm * 0.3937
    return round(inch, 3)
