"""find answer from given formula (F = ma)"""

m = float(input("Enter mass(kg)= "))
a = float(input("Enter acceleration(m/s^2) = "))
f = m * a
print(f"From mass = {m:.2f} kg and acceleration = {a:.2f} m/s^2")
print(f"Total force = {f:.2f} N")