"""find factors"""

number = int(input("Input number: "))
factors = []
for num in range(1, number + 1):
    if number % num == 0:
        factors.append(num)

print(f"Factors of {number} are ", end="")
if len(factors) > 0:
    for fac in factors:
        print(fac, end=" ")
else:
    print("None", end=" ")
print("")
print(f"Summation of factors is {sum(factors)}")