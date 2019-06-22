def buddhist_era_to_rattanakosin_era(buddhist):
    rattanakosin = buddhist - 2324
    return int(rattanakosin)


buddhist_era = int(input("Buddhist Era: "))
rattanakosin_era = buddhist_era_to_rattanakosin_era(buddhist_era)
print(f"{buddhist_era} Buddhist Era = {rattanakosin_era} Rattanakosin Era")