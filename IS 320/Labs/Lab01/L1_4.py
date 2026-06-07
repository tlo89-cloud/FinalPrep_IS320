'''
Python Lab 1
Name: Trevor Lorenz
Class: IS 320
Description: Lab Problem 4
'''

# Problem 4

'''
Prompts User for Name, weight in pounds of
coffee ordered, one by one

Outputs bulled amounts and receipt
'''

# Inputs
name = input('Enter your name \n >>')
weight = float(input("Enter the weight of order \n >>"))

# Initilization
cost_per_pound_coffee = 18.5
tax_rate = .07
shipping_cost_per_pound = .75

# Computations
order_price = cost_per_pound_coffee * weight
ship = shipping_cost_per_pound * weight
tax = order_price * tax_rate
billed = order_price + + ship + tax

# Outputs
print(f"Hello {name:s}, you ordered {weight:.2f} pounds of coffee,")
print(f"and you owe {billed:.2f}$, including {ship:.2f}$ for shipping, and {tax:.2f}$ tax")
