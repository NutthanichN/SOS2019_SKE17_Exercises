"""election"""

age = int(input("How old are you? "))
while age < 18:
    age = int(input("How old are you? "))
print("Congratulations! You can vote in the election.")