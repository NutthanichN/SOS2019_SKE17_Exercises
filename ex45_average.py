def average(lst):
    for i in lst:
        if not isinstance(i, int):
            return "This is not a list of integers."
    return sum(lst) / len(lst)
