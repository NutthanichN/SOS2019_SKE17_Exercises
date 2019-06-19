"""print even numbers"""

number = int(input("Number: "))
for num in range(0, number + 1, 2):
    print(num, end=" ")