'''midterm problem 1

Problem 1: 

SUBMIT
user inputs:  income, married or not (1/0)
displayed output: tax
tax rate:  married:   0.3 above 150000  0.2 otherwise
    not married:  0.2 above 100000 0.15 otherwise
function:  compute tax.  performs two steps 1. figure out the tax rate  2. calculate the tax.

SUMMARY
displays:  average tax,   average tax for married people
functions:  one for each average.

RESET
gets ready for new series of inputs
'''


# globals
total_tax = 0.0
total_tax_count = 0
total_married_tax = 0.0
total_married_tax_count = 0


# functions

def submit():
    global total_tax, total_tax_count, total_married_tax, total_married_tax_count
    
    income = int(input("Enter income here >>> "))
    while income < 0:
        print(f"You entered {income:.1f}, please enter a positive value")
        income = int(input("Enter a positive income here >>> "))
    married = int(input("Married (1) or not (0): >>> "))

    tax, tax_rate = compute_results(income, married)
    
    print(f"Tax Rate: {tax_rate:.2f}")
    print(f"Tax: {tax:.2f}")


def compute_results(income, married):
    global total_tax, total_tax_count, total_married_tax, total_married_tax_count
    if married:
        if income > 150000:
            tax_rate = 0.30
        else:
            tax_rate = 0.20
        tax = income * tax_rate
        total_married_tax += tax
        total_married_tax_count += 1
    else:
        if income > 100000:
            tax_rate = 0.20
        else:
            tax_rate = 0.15
        tax = income * tax_rate
    total_tax += tax
    total_tax_count += 1
    return tax, tax_rate


def compute_total_avg_tax():
    global total_tax, total_tax_count, total_married_tax, total_married_tax_count
    if total_tax_count == 0:
       return "No Data"
    else:
        average_tax = total_tax / total_tax_count
        return average_tax


def compute_total_avg_married_tax():
    global total_tax, total_tax_count, total_married_tax, total_married_tax_count
    if total_married_tax_count == 0:
        return "No Data"
    else:
        average_tax_married = total_married_tax / total_married_tax_count
        return average_tax_married


def summary():
    global total_tax, total_tax_count, total_married_tax, total_married_tax_count
    average_tax = compute_total_avg_tax()
    average_tax_married = compute_total_avg_married_tax()

    print(f"Avg tax: {average_tax}")
    print(f"Avg Married tax: {average_tax_married}")


def reset():
    global total_tax, total_tax_count, total_married_tax, total_married_tax_count
    total_tax = 0.0
    total_tax_count = 0
    total_married_tax = 0.0
    total_married_tax_count = 0
    print("Ready for new data!")


quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset. 4.Exit')
   print('Choose 1,2,3, or 4')
   choice = int(input('>>'))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       quit = True
   else:
       print('Invalid choice! Choose 1,2,3, or 4')
print('Bye!')
