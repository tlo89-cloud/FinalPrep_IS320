"""Lec8App0
compute tax at 10%
submit: input: income(float)
output: tax(float)
summary: output: average_tax float
"""

# globals
total_tax = 0.0 # sum of taxes, for avg tac
count = 0


# functions
def compute_average_tax():
    global total_tax, count

    if count > 0:   # apparently this will be mandatory (0 division protection)
        avg = total_tax / count
    else:
        avg = None      # same here
    return avg


def submit():
    # global call
    global total_tax, count
    # inputs
    income = float(input('Enter income >'))

    # computations

    # A process current inputs
    tax_rate = 0.1
    tax = income * tax_rate

    #B update globals
    total_tax += tax
    count += 1
    #outputs
    print(income)
    print(tax)
    #end submit


def summary():
    average_tax = compute_average_tax()
    if average_tax is not None:
        print(f"your average is {average_tax:.2f}\nNumber of Inputs: {count:d}")
    else:
        print("No data to compute and allat")

#end summary


def reset():
    global total_tax, count
    total_tax = 0.0
    count = 0


#main
quit = False
if not quit:
    print("1. Submit 2. Summary 3. Quit")

    choice = int(input("Enter 1, 2, 3, or 4>>\t"))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print("Ready for a new series of data")
    elif choice == 4:
        quit = True
    else:
        print("Invalid decision")

print("Goodbye!")


#NOTES
#Ask two questions before making a variable global:
# 1: does the variable need to remember its value after the function is over:
# 2: does the variable need to be 'seen' by multiple functions:
#the answer to at least one must be YES before making a variable global.
#set up globals at the top,
#one variable per lne,
#each with a comment,
#each initialized (showing type where necessary - eg total_tax = 0.0)
#as soon as you set up a global var,
# add the 'global...' line to functions.
# which functions?
# - safe: all functions. when you add a new function later, start with global....
# - best practice: use in functions which use the globals.
# - must: functions which *modify* the global variables.
#<<do not send global variables as parameters to the function
# none is not a number, it has its own type.

# if is_graded == 1: is the same as    if is_graded
# if is_graded == 0: is the same as    if not is_graded