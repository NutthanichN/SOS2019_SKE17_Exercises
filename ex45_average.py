def average(lst):
    """compute an average of a list of numbers

    >>> average([1, 2, 3, 4])
    2.5
    >>> average([-5, -20, 13, 4])
    -2.0
    >>> average([1, 2, 3, 'cat'])
    This is not a list of numbers
    >>> average(['1', '2', '3', '4'])
    This is not a list of numbers
    >>> average([' '])
    This is not a list of numbers

    """
    for i in lst:
        if isinstance(i, str):
            return "This is not a list of numbers"
    avg = sum(lst) / len(lst)
    return avg
