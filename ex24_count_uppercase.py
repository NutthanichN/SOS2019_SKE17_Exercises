"""count uppercase"""

text = input("Enter text: ")
count = 0
for char in text:
    if char != " " and char == char.upper():
        count += 1
print(f"There is(are) {count} uppercase(s).")