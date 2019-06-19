"""election"""

age = int(input("How old are you? "))
while age < 18:
    age = int(input("How old are you? "))
print("Congratulation! You can vote in the election.")