""" Trevor Lorenz Lab 03 Problem 4 04/29/2026.

Collects four inputs from user: income, married or not (1 or 0),
number of exemptions claimed, number of children (last 2 could be 0)

An individual can claim up to 3 exemptions, for singles, each exemption
worth 350$, married, each is worth 500$

Total exemption amount subtracted from income to compute taxable income
then calculate tax_rate, then calculate tax, then calculate deductions based
on marital status and number of children, subtract this from tax to get tax rate,
if this drives tax below zero, tax is 0. Output tax

input: income (float), marital_status (int), exemption_count (int), num_children (int)
output: tax (float)
"""


# functions
def compute_taxable_income(income, marital_status, exemption_count):
    if marital_status == 0:
        total_exemptions = exemption_count * 350.0
    else:
        total_exemptions = exemption_count * 500.0
    taxable_income = income - total_exemptions

    return taxable_income


def compute_tax_rate(taxable_income, marital_status):
    if marital_status == 0:
        if taxable_income >= 100000.0:
            tax_rate = 0.20
        else:
            tax_rate = 0.15
    else:
        if taxable_income > 150000.0:
            tax_rate = 0.25
        else:
            tax_rate = 0.20

    return tax_rate


def compute_deduction(marital_status, num_children):
    if marital_status == 1:
        num_deductions = num_children + 1
    else:
        num_deductions = num_children + 2
    deduction = num_deductions * 1000.0
    return deduction


# main

# inputs
income = float(input("Input income\n>>>"))
marital_status = int(input("Married or not (1 or 0 respectively)\n>>>"))
exemption_count = int(input("Number of exemptions claimed (0,1,2,3)\n>>>"))
num_children = int(input("Number of children\n>>>"))


# computations
taxable_income = compute_taxable_income(income, marital_status,
                                        exemption_count)
tax_rate = compute_tax_rate(taxable_income, marital_status)

tax = taxable_income * tax_rate

deduction = compute_deduction(marital_status, num_children)

tax = tax - deduction

if tax < 0:
    tax = 0

# outputs
print(f"Tax: {tax:.2f}")
