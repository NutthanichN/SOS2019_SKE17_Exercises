def cal_centripetal_force(m, v, r):
    f = (m * (v**2)) / r
    return round(f, 2)


mass = float(input("mass (kg) = "))
velocity = float(input("velocity (m/s) = "))
radius = float(input("radius (m) = "))
force_c = cal_centripetal_force(mass, velocity, radius)
print(f"From m = {mass:.2f} kg, v = {velocity:.2f} m/s and r = {radius:.2f} m")
print(f"The centripetal force = {force_c:.2f} N")