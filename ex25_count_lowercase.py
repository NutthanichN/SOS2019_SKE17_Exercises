"""count lowercase"""

text = input("Enter text: ")
count = 0
for char in text:
    if char != " " and char == char.lower():
        count += 1
print(f"There is(are) {count} lowercase(s).")