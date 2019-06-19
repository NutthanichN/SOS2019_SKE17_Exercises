"""find a length of input string"""

text = input("Enter text: ")
count = 0
for i in text:
    count += 1
print(f"A length of this text is {count}")