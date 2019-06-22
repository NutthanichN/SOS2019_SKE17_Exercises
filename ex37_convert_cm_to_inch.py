def centimeters_to_inches(cm):
    inch = cm * 0.3937
    return round(inch, 3)


cm = float(input("Enter number (in centimeters): "))
inch = centimeters_to_inches(cm)
print(f"{cm:.3f} centimeters = {inch:.3f} inches")