"""
Problem one and shi


"""


# globals
count_tax = 0
total_tax = 0.0
count_married_tax = 0
total_married_tax = 0

# functions

def compute_results(income, married):
    global count_tax, total_tax, count_married_tax, total_married_tax
    if married:
        if income > 150000.0:
            tax_rate = 0.30
        else:
            tax_rate = 0.20
        count_married_tax += 1
    else:
        if income > 100000.0:
            tax_rate = 0.20
        else:
            tax_rate = 0.15
    tax = income * tax_rate
    count_tax += 1
    total_tax += tax
    if married:
        total_married_tax += tax
    return tax, tax_rate


def submit():
    global count_tax, total_tax, count_married_tax, total_married_tax
    income = float(input("Type Income >>> "))
    while income < 0:
        print("income shouldnt be neg")
        income = float(input("Type POS Income >>> "))
    married = int(input("Type Married (1) or Not (0) >>> "))
    tax, tax_rate = compute_results(income, married)
    print(f"Your tax is: {tax:.2f}")
    print(f"your tax rate is : {tax_rate:.2f}")


def compute_avg_tax():
    global count_tax, total_tax, count_married_tax, total_married_tax
    if count_tax > 0:
        avg = total_tax / count_tax
    else:
        avg = None
    return avg


def compute_avg_married_tax():
    global count_tax, total_tax, count_married_tax, total_married_tax
    if count_married_tax > 0:
        avg = total_married_tax / count_married_tax
    else:
        avg = None
    return avg


def summary():
    global count_tax, total_tax, count_married_tax, total_married_tax
    avg_tax = compute_avg_tax()
    avg_married_tax = compute_avg_married_tax()

    if avg_tax is None:
        print("Not enough data to calc average tax")
    else:
        print(f"The average tax is {avg_tax:.2f}")
    
    if avg_married_tax is None:
        print("Not enough data to calc average tax")
    else:
        print(f"Average married tax is: {avg_married_tax:.2f}")


def reset():
    global count_tax, total_tax, count_married_tax, total_married_tax
    count_tax = 0
    total_tax = 0.0
    count_married_tax = 0
    total_married_tax = 0
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
