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
outputs: order_price, discount_amount, tax, shipping_cost,
         billed_amount (floats)

"""


# functions
# problem 1
def compute_order_price(wt):
    unit_price = 15.0
    price = wt * unit_price
    return price

# problem 2
def compute_discount(price):
    rate_discount = 0.03
    if price > 100.0:
        discount = price * rate_discount
    return discount


# problem 4
def calculate_tax(order_p):
    tax_rate = 0.08
    tax = tax_rate * order_p
    return tax


# problem 5
def find_ship_rate(wt):
    if wt <= 5.0:
        rate = 0.1
    elif wt <= 10.0:
        rate = 0.15
    else:
        rate = 0.2
    return rate


# problem 6
def find_ship_cost(wt, rt):
    cost = wt * rt
    return cost


# main
# inputs
weight = float(input('Enter weight in pounds >'))

# initializations
price_per_pound = 15.0
rate_discount = 0.03
tax_rate = 0.08

# computations
# 1 compute order price  out: order_price    in: weight
order_price = compute_order_price(weight)

# 2 find the discount, if any    out:discount_amount    in:order_price
discount_amount = compute_discount(order_price)

# 3 apply the discount
order_price -= discount_amount

# 4 compute tax  out: tax    in: order_price
tax = calculate_tax(order_price)

# 5 find shipping rate   out: rate_ship  in: weight
rate_ship = find_ship_rate(weight)

# 6 compute shipping cost    out: shipping_cost  in: weight, rate_ship

ship_cost = find_ship_cost(weight, rate_ship)

# 7 billed amount
billed = ship_cost + order_price + tax

# outputs

print(f'Weight {weight:.2f}')
print(f'Order price: {order_price:.2f}')
print(f'Discount: {discount_amount:.2f}')
print(f'Total price: {billed:.2f}')
