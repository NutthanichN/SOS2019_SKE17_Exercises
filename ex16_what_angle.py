"""What kind of this angle?"""

angle = float(input("Please enter angle(in degree unit): "))

if angle <= 0:
    print("The angle must be larger than 0")
elif 0 < angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif 90 < angle < 180:
    print("Obtuse angle")
elif angle == 180:
    print("Straight angle")
elif 180 < angle < 360:
    print("Reflex angle")
elif angle == 360:
    print("Full rotation")
