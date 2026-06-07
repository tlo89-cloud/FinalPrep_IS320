"""Lecture 4 App 1. Price computation.
User enters weight in pounds. App computes order price,
discount, at 3% when order price is above 100$,
tax at 8%, and shipping cost.
Shipping rate is 10 cents per pound up to and including 5 pounds,
15 cents upto and including 10 pounds, and 20 cents above that.
unit price is 15$ per pound.
Display order price, discount, tax, shipping cost, and the billed amount.
('order price' above does not include tax and shipping cost.)
input: weight (float)
outputs: order_price, discount_amount, tax, shipping_cost, billed_amount (floats)

"""
# inputs
weight = float(input('Enter weight in pounds >'))

# initializations
price_per_pound = 15.0
rate_discount = 0.03
tax_rate = 0.08

# computations
# 1 compute order price  out: order_price    in: weight
order_price = weight * price_per_pound

# 2 find the discount, if any    out:discount_amount in:order_price
if order_price > 100.0:
    discount_amount = order_price * rate_discount
else:
    discount_amount = 0.0

# 3 apply the discount
order_price -= discount_amount

# 4 compute tax  out: tax    in: order_price
tax = order_price * tax_rate

# 5 find shipping rate   out: rate_ship  in: weight
if weight <= 5.0:
    ship_rate_per_lbs = 0.10
elif weight <= 10:
    ship_rate_per_lbs = 0.15
else:
    ship_rate_per_lbs = 0.20

# 6 compute shipping cost    out: shipping_cost  in: weight, rate_ship

ship_cost = ship_rate_per_lbs * weight

# 7 billed amount
billed = ship_cost + order_price + tax

# outputs

print(f'Weight {weight:.1f}')
print(f'Order price: {order_price:.1f}')
print(f'Discount: {discount_amount:.1f}')
print(f'Total price: {billed:.1f}')
