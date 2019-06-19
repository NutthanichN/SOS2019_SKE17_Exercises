"""Is this TV cheap, medium price or expensive?"""

price = float(input("Enter a price: "))
if price > 100000:
    print("This TV is expensive.")
elif price >= 10000:
    print("This TV is moderate price.")
elif price > 0:
    print("This TV is cheap.")
else:
    print("A price must be greater than 0")