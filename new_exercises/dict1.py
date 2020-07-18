"""Write a program that receives 3 key-value pairs from the user and creates a dictionary.
Then prints that dictionary and shows its type like the examples below."""

my_dict = {}
pair1 = input("Enter the first key-value pairs separated by comma (,): ")
pair2 = input("Enter the second key-value pairs separated by comma (,): ")
pair3 = input("Enter the last key-value pairs separated by comma (,): ")

key1, value1 = pair1.split(",")
key2, value2 = pair2.split(",")
key3, value3 = pair3.split(",")

my_dict[key1] = value1
my_dict[key2] = value2
my_dict[key3] = value3

print(my_dict)
print(type(my_dict))
