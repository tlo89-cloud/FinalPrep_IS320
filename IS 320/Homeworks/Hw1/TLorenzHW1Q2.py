""" Trevor Lorenz Hw1 Question 2 04/06/2026.

User inputs name, weight (lbs) of coffee ordered,
and outputs the billed amount and receipt

input: name: str
input: weight: float

output: billed (float), shipping (float), tax (float)

"""

# Inputs
name = input('Enter your name \n >>')
weight = float(input("Enter the weight of order \n >>"))

# Initialization
cost_per_pound_coffee = 18.50
tax_rate = 0.07
shipping_cost_per_pound = 0.75

# Computations
order_price = cost_per_pound_coffee * weight
ship = shipping_cost_per_pound * weight
tax = order_price * tax_rate

billed = order_price + ship + tax

# Outputs
print(f"Hello {name:s}, you ordered {weight:.2f} pounds of coffee,")
print(f"and you owe {billed:.2f}$, including {ship:.2f}$ for shipping, and {tax:.2f}$ tax.")
