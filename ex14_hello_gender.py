"""say hello depend on gender"""

gender = input("What is your gender? (male/female): ")
if gender.lower() == 'male':
    print("Hello mister!")
elif gender.lower() == "female":
    print("Hello miss!")
else:
    print("Input must be male or female.")