"""Is a prime number?

positive integer = [1, inf)
non-negative integer = [0, inf)
negative integer = (-inf, -1]
non-positive integer = (-inf, 0]

"""

number = int(input("Number: "))
factors = []

if number < 0:
    print("Input number must be a non-negative integer.")
else:
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    if len(factors) == 2:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

