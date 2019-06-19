"""swap the first character and last character"""

text = input("Enter text: ")
print(text[-1] + text[1:-1] + text[0])
