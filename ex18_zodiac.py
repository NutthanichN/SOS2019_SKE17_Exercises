"""What is your zodiac sign?"""

day = int(input("Enter your birthday: "))
month = input("Enter your birth month(Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sep/Oct/Nov/Dec): ")

# map = {
#     "Jan": (19, 31, "Capricorn", "Aquarius"),
#     "Feb": (18, 29, "Aquarius", "Pisces"),
#     "Mar": (20, 31, "Pisces", "Aries"),
#     "Apr": (19, 30, "Aries", "Taurus"),
#     "May": (20, 31, "Taurus", "Gemini"),
#     "Jun": (20, 30, "Gemini", "Cancer"),
#     "Jul": (22, 31, "Cancer", "Leo"),
#     "Aug": (22, 31, "Leo", "Virgo"),
#     "Sep": (22, 30, "Virgo", "Libra"),
#     "Oct": (22, 31, "libra", "Scorpio"),
#     "Nov": (21, 30, "Scorpio", "Sagittarius"),
#     "Dec": (21, 31, "Sagittarius", "Capricorn")
# }
#
# try:
#     a, b, c, d = map[month]
#     if 0 < day <= a:
#         print(f"Your zodiac sign is {c}.")
#     elif a < day <= b:
#         print(f"Your zodiac sign is {d}.")
#     else:
#         print("There is no this day in this month.")
# except KeyError:
#     print("This month does not exist.")

if month == "Jan":
    if 0 < day <= 19:
        print("Your zodiac sign is Capricorn.")
    elif 19 < day <= 31:
        print("Your zodiac sign is Aquarius.")
    else:
        print("There is no this day in this month.")
elif month == "Feb":
    if 0 < day <= 18:
        print("Your zodiac sign is Aquarius.")
    elif 18 < day <= 29:
        print("Your zodiac sign is Pisces.")
    else:
        print("There is no this day in this month.")
elif month == "Mar":
    if 0 < day <= 20:
        print("Your zodiac sign is Pisces.")
    elif 20 < day <= 31:
        print("Your zodiac sign is Aries.")
    else:
        print("There is no this day in this month.")
elif month == "Apr":
    if 0 < day <= 19:
        print("Your zodiac sign is Aries.")
    elif 19 < day <= 30:
        print("Your zodiac sign is Taurus.")
    else:
        print("There is no this day in this month.")
elif month == "May":
    if 0 < day <= 20:
        print("Your zodiac sign is Taurus.")
    elif 20 < day <= 31:
        print("Your zodiac sign is Gemini.")
    else:
        print("There is no this day in this month.")
elif month == "Jun":
    if 0 < day <= 20:
        print("Your zodiac sign is Gemini.")
    elif 20 < day <= 30:
        print("Your zodiac sign is Cancer.")
    else:
        print("There is no this day in this month.")
elif month == "Jul":
    if 0 < day <= 22:
        print("Your zodiac sign is Cancer.")
    elif 22 < day <= 31:
        print("Your zodiac sign is Leo.")
    else:
        print("There is no this day in this month.")
elif month == "Aug":
    if 0 < day <= 22:
        print("Your zodiac sign is Leo.")
    elif 22 < day <= 31:
        print("Your zodiac sign is Virgo.")
    else:
        print("There is no this day in this month.")
elif month == "Sep":
    if 0 < day <= 22:
        print("Your zodiac sign is Virgo.")
    elif 22 < day <= 30:
        print("Your zodiac sign is Libra.")
    else:
        print("There is no this day in this month.")
elif month == "Oct":
    if 0 < day <= 22:
        print("Your zodiac sign is Libra.")
    elif 22 < day <= 31:
        print("Your zodiac sign is Scorpio.")
    else:
        print("There is no this day in this month.")
elif month == "Nov":
    if 0 < day <= 21:
        print("Your zodiac sign is Scorpio.")
    elif 21 < day <= 30:
        print("Your zodiac sign is Sagittarius.")
    else:
        print("There is no this day in this month.")
elif month == "Dec":
    if 0 < day <= 21:
        print("Your zodiac sign is Sagittarius.")
    elif 21 < day <= 31:
        print("Your zodiac sign is Capricorn.")
    else:
        print("There is no this day in this month.")
else:
    print("This month does not exist.")
