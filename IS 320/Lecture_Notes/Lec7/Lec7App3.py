''' Trevor Lorenz Lec7 Problem 1

Specification:  User enters income.  Tax rate is 10% at or below 100,000
dollars, 15% otherwise.

Use two functions, one for tax rate and the other for tax, and display tax.

Extended Spec:  Modify the program to support multiple inputs, and compute the
average tax across this series of inputs.

'''
# global variables: REQUIRED FOR HW AND TESTS TO HAVE THIS AND COMMENT
total_tax = 0.0  # sum of taxes, for computing avg tax
count = 0


# functions
def find_tax_rate(income):
    if income <= 100000.0:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    return tax_rate


def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax


def submit():
    # main
    global total_tax, count
    income = float(input("Enter income\n >>>"))

    # 1 find the tax rate   out: tax_rate   in: income - floats

    # compute the tax:    out: tax  in: income, tax_rate - floats
    tax_rate = find_tax_rate(income)
    tax = calculate_tax(income, tax_rate)
    # update totals

    total_tax += tax
    count += 1

    print(income)
    print(tax)
    print(total_tax)

# end submit


def compute_average_tax():
    global total_tax, count

    avg = total_tax / count
    return avg


def summary():
    global total_tax, count
    average_tax = compute_average_tax()
    print(average_tax)


submit()
submit()
submit()
summary()
# by making the whole calc part a funtion, we made globals
# locals, which is good for memory
# modularity, code reuse, hide details
