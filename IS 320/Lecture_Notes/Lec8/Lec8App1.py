"""Lec8App1 Revision of Lec5App1
unit_price = 15.0 < input is weight.
rate_discount = 0.03 <above 100 price gets discount
tax_rate = 0.08 < tax is based on price
submit: output: price, discount, tax, billed
summary: output: average_price, discount_count, no_discount_count
"""

# globals
total_price = 0.0 # sum of order prices, for average price
num_orders = 0 # count orders, for average price
discount_count = 0 # count the orders that get a discount


# functions


def compute_order_price(wt):
    unit_price = 15.0
    price = wt * unit_price

    return price


def compute_discount(price):
    rate_discount = 0.03
    discount = 0.0
    if price > 100.0:
        discount = price * rate_discount

    return discount


def compute_tax(price):
    tax_rate = 0.08
    tax = price * tax_rate

    return tax


def submit():
    pass

def summary():
    global total_price, num_orders, discount_count
    no_discount_count = num_orders - discount_count
    average_price = compute_average_price()

    if average_price is not None:
        print(f'Average price {average_price:.2f}')
    else:
        print("No data available for average price")
        print(total_price, discount_count, no_discount_count)


def reset():
    pass

# inputs
weight = float(input('Enter weight in lbs >'))

# computations
# price
order_price = compute_order_price(weight)
# discount
discount_amount = compute_discount(order_price)
# apply the discount
order_price = order_price - discount_amount
# compute tax
tax = compute_tax(order_price)
# find the shipping rate
# compute shipping cost
# billed
billed_amount = order_price + tax
# update globals
total_price += order_price
num_orders += 1

if discount_amount > 0.0:
    discount_amount

# outputs
print(f'''
        Weight:\t{weight:.1f}
        Price:\t{order_price:.2f}
        Discount:\t{discount_amount:.2f}
        Tax:\t\t{tax:.2f}
        Billed:\t{billed_amount:.2f}
''')

def compute_average_price():
    global total_price, num_orders
    if num_orders > 0:
        avg = total_price / num_orders
    else:
        avg = None
    return avg

# main


def main():
    quit = False
    while not quit:
        print('1.Submit 2.Summary 3.Reset 4. Exit')
        choice = int(input('Enter 1, 2, 3 or 4 >'))
        if choice == 1:
            submit()
        elif choice == 2:
            summary()
        elif choice == 3:
            reset()
            print('Ready for a new series...')
        elif choice == 4:
            quit = True
        else:
            print('Invalid choice!')
    print('Goodbye!')
# if a global can be derived from others,
# then it does not really need to be global
# if multiple averages are to be computed,
# we can do separate functions, checking for zero division
# for each average. and the summary may need multiple if statements.
# that is if the averages are entirely independent of each other.
# if the averages are interdependent, the if statements in summary may
# need to be connected.
