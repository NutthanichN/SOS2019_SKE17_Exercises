"""print transcript"""

eng_credit = 3
physics_credit = 3
thai_credit = 2
total_credit = eng_credit + physics_credit + thai_credit

name1 = "Min"
eng1 = 70
physics1 = 81
thai1 = 85
gpa1 = ((eng1 * eng_credit) + (physics1 * physics_credit) + (thai1 * thai_credit)) / total_credit

name2 = "Pim"
eng2 = 89
physics2 = 82
thai2 = 76
gpa2 = ((eng2 * eng_credit) + (physics2 * physics_credit) + (thai2 * thai_credit)) / total_credit

name3 = "Mind"
eng3 = 78
physics3 = 69
thai3 = 79
gpa3 = ((eng3 * eng_credit) + (physics3 * physics_credit) + (thai3 * thai_credit)) / total_credit

print("-------------------------------------------------------------------------------")
print("| name | English (3 credits) | Physics (3 credits) | Thai (2 credits) |  GPA  |")
print("-------------------------------------------------------------------------------")
print(f"| {name1:<5}| {eng1:^20}| {physics1:^20}| {thai1:^17}| {gpa1:^6.2f}|")
print("-------------------------------------------------------------------------------")
print(f"| {name2:<5}| {eng2:^20}| {physics2:^20}| {thai2:^17}| {gpa2:^6.2f}|")
print("-------------------------------------------------------------------------------")
print(f"| {name3:<5}| {eng3:^20}| {physics3:^20}| {thai3:^17}| {gpa3:^6.2f}|")
print("-------------------------------------------------------------------------------")


