x = 10
y = 5.5

'''
Whole numbers -> integers -> int
10, 0, -10
Real numbers -> floating point numbers -> float
5.5, 10.0, 0.0, -10.0

weight - float
volumne

'''

'''
Lec2App1 04.02.26 Developed by Trevor

User enters name, income. App displays tax at 8%

inputs name(string)    income(float)
outputs    tax(float)
'''

# what are the variables?
# a. inputs name(string)    income(float)
# b. outputs    tax(float)

'''
variable names:
rules: letters, _, digits only
conventions: lower case only, informative names
use digits only if you must
snake_casing is tax_rate (we use this)
camelCasing is taxRate
'''

# Inputs
name = "Alex"
income = 1500.0

# Initializations
tax_rate = 0.08

# Computations
tax = income * tax_rate

# Outputs
print(f"Hello {name:s}, your income was {income:f} dollars")
print(f"Hello {name:s}, your tax was {tax:2f} dollars")

# Note: str = s, float .xf x digits after decimal point. x = 2 for money
# int = d