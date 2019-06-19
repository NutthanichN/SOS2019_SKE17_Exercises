"""count consonants"""

text = input("Enter your text: ")
count = 0
for char in text:
    if char.isalpha():
        if char != " " and char not in 'AaEeIiOoUu':
            count += 1
print(f"This text has {count} consonant(s).")