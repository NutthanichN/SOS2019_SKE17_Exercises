"""sum of input number"""

number = float(input("Enter a number: "))
sum = number
while sum <= 100:
    number = float(input("Enter a number: "))
    sum += number
print(f"Summation = {sum:.2f}")

