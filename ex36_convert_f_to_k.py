def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * (5/9)
    return round(kelvin, 2)


fahrenheit = float(input("Enter temperature (in Fahrenheit): "))
kelvin = fahrenheit_to_kelvin(fahrenheit)
print(f"{fahrenheit:.2f} Fahrenheit = {kelvin:.2f} Kelvin")