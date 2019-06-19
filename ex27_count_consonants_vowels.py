"""count consonants and vowels"""

text = input("Enter your text: ")
count_consonant = 0
count_vowel = 0
for char in text:
    if char.isalpha():
        if char not in 'AaEeIiOoUu':
            count_consonant += 1
        else:
            count_vowel += 1
print(f"This text has {count_consonant} consonant(s) and {count_vowel} vowel(s).")