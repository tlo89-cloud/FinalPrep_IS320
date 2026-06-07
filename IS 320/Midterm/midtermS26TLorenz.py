"""   Trevor Lorenz  """
#include your name in the filename as well 
# midtermS26JSmith.py (or JohnS) if your name is  John Smith


#globals
count_total_tax = 0
total_tax = 0.0
count_unmarried_tax = 0
total_unmarried_tax = 0.0
count_married_tax = 0


#functions

def compute_tax(income, married):
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    if married:
        count_married_tax += 1
        if income >= 50000:
            tax_rate = 0.10
        else:
            tax_rate = 0.08
    else:
        count_unmarried_tax += 1
        if income > 70000:
            tax_rate = 0.07
        else:
            tax_rate = 0.05
    tax = income * tax_rate
    count_total_tax += 1
    return tax, tax_rate


def compute_child_credit(married, count_of_child_credits):
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    if married:
        child_credit = count_of_child_credits * 1500
    else:
        child_credit = count_of_child_credits * 2000
    return child_credit


def compute_results(income, married, count_of_child_credits):
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    tax, tax_rate = compute_tax(income, married)
    child_credit = compute_child_credit(married, count_of_child_credits)
    actual_tax = tax - child_credit
    
    if actual_tax < 0:
        actual_tax = 0

    if not married:
        total_unmarried_tax += actual_tax

    total_tax += actual_tax
    non_fraction_tax_rate = tax_rate * 100

    return  actual_tax, non_fraction_tax_rate, child_credit


def submit():
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    income = float(input("Income >>>"))

    married = int(input("Enter 1 for married, 0 if not >>>"))
    while married < 0 or married > 1:
        print(f"You entered {married:d}, input needs to be 1 or 0")
        married = int(input("Enter 1 for married, 0 if not >>>"))

    count_of_child_credits = int(input("Number of child credits claimed >>>"))
    while count_of_child_credits < 0 or count_of_child_credits > 5:
        print(f"You input {count_of_child_credits:d}, please input a number 0-5")
        count_of_child_credits = int(input("Number of child credits claimed (enter 0-5)>>>"))

    actual_tax, non_fraction_tax_rate, child_credit = compute_results(income, married, count_of_child_credits)

    print(f"Tax:\t\t {actual_tax:.2f}")
    print(f"Tax Rate:\t {non_fraction_tax_rate:.2f}")
    print(f"Child Credit:\t {child_credit:.2f}")
        

def calculate_total_and_unmarried_avgs():
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    if count_unmarried_tax > 0:
        avg_unmarried_tax = total_unmarried_tax / count_unmarried_tax
    else:
        avg_unmarried_tax = None
    if count_total_tax > 0:
        avg_total_tax = total_tax / count_total_tax
    else:
        avg_total_tax = None
    return avg_unmarried_tax, avg_total_tax


def summary():
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    avg_unmarried_tax, avg_total_tax = calculate_total_and_unmarried_avgs()
    
    if avg_total_tax is None:
        print("Not enough data to calculate average tax")
    else:
        print(f"Average Tax is: {avg_total_tax:.2f}")
    
    if avg_unmarried_tax is None:
        print("Not enough data to calculate avg unmarried tax")
    else:
        print(f"Average Unmarried Tax is: {avg_unmarried_tax:.2f}")

    print(f"Number of married taxpayers: {count_married_tax:d}")
    

def reset():
    global count_total_tax, total_tax, count_unmarried_tax, total_unmarried_tax, count_married_tax
    count_total_tax = 0
    total_tax = 0.0
    count_unmarried_tax = 0
    total_unmarried_tax = 0.0
    count_married_tax = 0


#main
quit = False
while not quit:
    print('1.Submit 2.Summary 3.Reset. 4.Exit')
    print('Choose 1,2,3 or 4')
    choice = int(input('>>'))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print('Ready for new series..')
    elif choice == 4:
        quit = True
    else:
        print('Invalid choice! Choose 1,2,3 or 4')

print('Bye!')