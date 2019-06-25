"""print transcript

Hint: In the first row, the words are all separated by one space except for 'GPA' which is separated by two spaces
      (i.e. similar to '|_name_|_English_(3_credits)_|_Physics_(3_credits)_|_Thai_(2_credits)_|__GPA__|').
      The numbers are in the middle of the cell.
"""

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
print(f"|{name1:^6}|{eng1:^21}|{physics1:^21}|{thai1:^18}|{gpa1:^7.2f}|")
print("-------------------------------------------------------------------------------")
print(f"|{name2:^6}|{eng2:^21}|{physics2:^21}|{thai2:^18}|{gpa2:^7.2f}|")
print("-------------------------------------------------------------------------------")
print(f"|{name3:^6}|{eng3:^21}|{physics3:^21}|{thai3:^18}|{gpa3:^7.2f}|")
print("-------------------------------------------------------------------------------")


