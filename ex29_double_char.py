"""double character"""

text = input("Input text: ")
double_char = ""
for char in text:
    double_char += char * 2
print(double_char)