""" Trevor Lorenz Lab2 Problem 1 04/09/2026.

User inputs lbs ordered of artichokes, carrots, and beets
Orders that total over $100 get 4% discount
program outputs their respective weights, and total
calories.

Shipping calculated on total weight, 5.50$ for 10 pounds 
or below, 10$ for  20 pounds or below, and 9.5$ plus 10c 
per pound,  for weights above 20 pounds.

input: lbs of artichokes (art)
input: lbs of carrots
input: lbs of beets
"""

# inputs
lbs_art = float(input("Input Pounds of Artichokes\n>>>"))
lbs_carrot = float(input("Input Pounds of Carrots\n>>>"))
lbs_beets = float(input("Input Pounds of Beets\n>>>"))


# initilization
arti_price_per_lbs = 2.67
carrot_price_per_lbs = 1.89
beet_price_per_lbs = 0.79

total_weight = lbs_art + lbs_carrot + lbs_beets

discount = .04

# computations
cost_of_art = lbs_art * arti_price_per_lbs
cost_of_carrots = lbs_carrot * carrot_price_per_lbs
cost_of_beets = lbs_beets * beet_price_per_lbs

total_order_price = cost_of_art + cost_of_beets + cost_of_carrots

if total_order_price > 100.0:
    preship_order_price = total_order_price * (1 - discount)
else:
    preship_order_price = total_order_price

if total_weight <= 10.0:
    ship_cost = 5.50
elif total_weight <= 20.0:
    ship_cost = 10.0
else:
    ship_cost = 9.5 + total_weight * .10

billed_amount = preship_order_price + ship_cost

# output

print(f"Price: {preship_order_price:.2f}")
print(f"Shipping charge: {ship_cost:.2f}")
print(f"Billed amount: {billed_amount:.2f}")
