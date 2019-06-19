"""make square"""

size = int(input("Enter a size of square: "))
i = 0
while i < size:
    j = 0
    while j < size:
        j += 1
        print("*", end=" ")
    i += 1
    print("")