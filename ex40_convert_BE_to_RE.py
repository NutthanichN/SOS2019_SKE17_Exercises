def buddhist_era_to_rattanakosin_era(buddhist):
    """convert Buddhist Era to Rattanakosin Era

    >>> buddhist_era_to_rattanakosin_era(2561)
    237
    >>> buddhist_era_to_rattanakosin_era(3600.43)
    1276
    >>> buddhist_era_to_rattanakosin_era(500)
    -1824
    >>> buddhist_era_to_rattanakosin_era(0)
    -2324
    >>> buddhist_era_to_rattanakosin_era(-1500)
    -3824
    """
    rattanakosin = buddhist - 2324
    return int(rattanakosin)
