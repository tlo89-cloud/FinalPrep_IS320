"""
Lab 2 Drill 3: create and use a function named highest() that takes three inputs and returns 
the highest number. After you have got it working, try calling the function with inputs 
‘hat’, ‘cat’, ‘rat’.

"""

def highest(inp1, inp2, inp3):
    if inp1 > inp2:
        if inp1 > inp3:
            highest = inp1
        else:
            highest = inp3
    elif inp2 > inp3:
        highest = inp2

'''
Problem 1
The user supplies information about marital status, and income, and your app computes and displays tax.  
Tax computation rule:
If Married,     tax rate is 20% for income above 200,000 dollars,
                           15% for others.
If Not Married,  tax rate is 15% for income above 100,000 dollars,
10% for others.
'''

income = int(input("income>"))
married = int(input("married (1), not (0)"))

def find_tax_rate(income, married):
    if married:
        if income > 200000.0:
            tax_rate = 0.20
        else:
            tax_rate = 0.15
    else:
        if income > 100000.0:
            tax_rate = 0.15
        else:
            tax_rate = 0.10
    return tax_rate


def compute_tax(income, tax_rate):
    tax = income * tax_rate
    return tax

tax_rate = find_tax_rate(income, married)
print(tax_rate)

print(compute_tax(income, tax_rate))
'''
In a library, members receive points for the books they read.
First three books read receive 10 points each.
Next three receive 15 points each. 
Every book after that receives 20 points each.
(So if 4 books are read by a particular member, 10 for first three, 
and 15 for the fourth, gives 45 points to the member.)


The user enters a member name, and number of books read;  the app 
displays the name, and points earned.
'''

name = input("Name>>")
num_books = int(input("Num books>>"))

def calc_points(num_books):
    if num_books <= 3:
        points = num_books * 10
    elif num_books <= 6:
        points = 3 * 10 + (num_books - 3) * 15
    else:
        points = 3 * 10 + 3 * 15 + (num_books - 6) * 20
    return points

points = calc_points(num_books)
print(f"Name: {name:s} read {num_books:d}, and got {points:d}")

"""
Problem 4
Parameters:   taxable_income function ← married, income, exemption_count
Tax_rate function ← taxable income, married
Deduction function ← married, child count
If statements -
Taxable income and deduction functions -  take the multiplication 
outside the if. Choose the unit amount for married/unmarried within 
the if (exemption, or unit_deduction), and then multiply by the count outside.

Tax rate - nested if is the most efficient and most readable. 


"""
married = int(input("married 1 or not 0"))
income = int(input("enter income"))
exemption_count = int(input("exemption count>>"))


def calc_taxable_inc():
    