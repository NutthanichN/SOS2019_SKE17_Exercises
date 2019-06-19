"""Is prime numbers?"""

number = int(input("Number: "))
factors = []

if number < 0:
    print("Input number must be a positive integer.")
else:
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    if len(factors) == 2:
        print(f"{number} is prime numbers.")
    else:
        print(f"{number} is not prime numbers.")

