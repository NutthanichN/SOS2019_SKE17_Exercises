"""say hello n times"""

times = int(input("How many times?: "))
if times <= 0:
    print("Input number must be a positive integer.")
else:
    for i in range(times):
        print("Hello!")