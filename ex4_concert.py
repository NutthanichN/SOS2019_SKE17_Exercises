"""concert"""

people = int(input("How many people?: "))
ticket_price = int(input("What is the ticket price? (4500/2500/1500): "))
total_price = people * ticket_price
print(f"Total price is {int(total_price)}")