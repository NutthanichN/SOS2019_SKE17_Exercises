"""Calculate an area of triangle"""

base = float(input("Enter base: "))
height = float(input("Enter height: "))

if base < 0 or height < 0:
    print("Base and height must be positive.")
else:
    area = (1/2) * base * height
    print(f"Area of triangle is {int(area)}")