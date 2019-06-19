"""bakery shop"""

red_velvet = int(input("How many Red Velvet Cakes?: "))
pana_cotta = int(input("How many Pana Cottas?: "))
cheese_pie = int(input("How many Cheese Pies?: "))

red_velvet_price = 130
pana_cotta_price = 90
cheese_pie_price = 145

if red_velvet < 0 or pana_cotta < 0 or cheese_pie < 0:
    print("Input number must be a positive integer.")
else:
    total_price = (red_velvet * red_velvet_price) + (pana_cotta * pana_cotta_price) + (cheese_pie * cheese_pie_price)
    total_stamp = total_price // 100
    print(f"Total price = {total_price}")
    print(f"Total stamps = {total_stamp}")