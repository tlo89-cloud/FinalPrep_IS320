""" Trevor Lorenz A1 Question 1 04/14/2026.

User enters weight ordered (in pounds).  User also specifies mode of shipment
(express or standard) by typing in 1 for express and 0 for standard shipping.
(Every order is either express, or standard shipment.
"""

# inputs
weight = float(input("Enter weight (lbs): "))
shipment_type = int(input("Enter shipment type (1: express, 0: standard): "))

# initilizations
unit_price_per_lb = 5.0
discount_rate = 0.02

# computations
# price based on units
price = unit_price_per_lb * weight

# discount eligibility
if price >= 50.0:
    discount = discount_rate * price
else:
    discount = 0

# price after discount
order_price = price - discount

# cost of shipping
if shipment_type == 1:
    if weight < 10.0:
        ship_cost = 0.25 * weight
    else:
        ship_cost = 0.30 * weight
else:
    if weight <= 20.0:
        ship_cost = 0.10 * weight
    else:
        ship_cost = 0.20 * weight

# output
print(f"Order price: {order_price:.2f}")
print(f"Discount amount: {discount:.2f}")
print(f"Shipping cost: {ship_cost:.2f}")
