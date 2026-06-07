'''
Q1: user enters income. app displays tax.
tax rate is 10% if the income is less than 100,000.
20% otherwise.

Input: flot
Output: Tax:
'''

'''
# inputs
income = float(input("Enter income, in dollars >"))


# computations
# 1 find tax rate   out: tax_rate (float)   in: income
# 2 compute the tax out: tax (float)    in: incomel, tax_rate
if income < 100000.0:
    tax_rate = .01
else:
    tax_rate = .02


tax = income * tax_rate

# outputs
print(f'income:\t {income:.2f}\nTax:\t{tax:.2f}')


'''


'''
Q2: user enters weight(in pounds). app displays shipping cost.
ship rate is 10 cents per lb for weights below 10 pounds,
15 cents per pound otherwise.
App 2:
User enters score (integer in range 0..100)
letter grade A,B or C is computed and displayed.
80-100 A
60-79 B
0-59 C
'''
# inputs


# computations
weight = float(input("Enter weight in lb >"))

# 1 find the shipping rate    out: rate_ship  in:weight (floats)
if weight <= 10.0:
    rate_ship = 0.1
else:
    rate_ship = 0.15
# 2 compute the shipping cost
ship_cost = rate_ship * weight

# outputs
print(f'Weight\t\t:{weight:.1f}')
print(f'Shipping Cost\t: {ship_cost:.2f}')
