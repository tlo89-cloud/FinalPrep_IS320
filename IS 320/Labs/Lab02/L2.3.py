""" Trevor Lorenz Lab2 Problem 3 04/09/2026.

User inputs weekly sales ($) for a salesperson, and the app will
determine commission and total pay for that salesperson

Commission earned when sales are >= 1000, at a rate of 15%

input: weekly sales: float
output: commission: float
output: total pay: float
"""

# inputs
weekly_sales = float(input("Type weekly sales:\n>>>"))

# initilization
base_salary = 250.0
commission_quota = 1000.0
commission_rate = 0.15

# computations
if weekly_sales >= commission_quota:
    commission = weekly_sales * commission_rate
else:
    commission = 0.0

total_pay = base_salary + commission

# output
if commission > 0.0:
    print(f"Commission: {commission:.2f}")
print(f"Total pay: {total_pay:.2f}")
