def average(lst):
    for i in lst:
        if not isinstance(i, int):
            return "This is not a list of integer"
    return sum(lst) / len(lst)
