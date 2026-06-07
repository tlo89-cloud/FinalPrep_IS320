""" Trevor Lorenz Lab2 Problem 2 04/09/2026.

Prompt user to input 2 integers, one by one, then test
if one or both or neither is the factor of another

input: int_1: integer
input: int_2: integer

"""

# inputs

int_1 = int(input("Please input the first integer:\n>>>"))
int_2 = int(input("Please input the second integer:\n>>>"))

if int_1 == 0:
    print("Invalid input")
elif int_2 == 0:
    print("Invalid input")
else:
    if int_2 % int_1 == 0:
        if int_1 % int_2 == 0:
            print("each is a factor of the other")
        else:
            print(f"{int_1} is a factor of {int_2}")
    elif int_1 % int_2 == 0:
        print(f"{int_2} is a factor of {int_1}")
    else:
        print("Neither is a factor of the other")
