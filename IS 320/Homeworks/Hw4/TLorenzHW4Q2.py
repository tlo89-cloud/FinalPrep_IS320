""" Trevor Lorenz HW 4 Problem 2 05/01/2026.

Collects two inputs from user, total books ordered and order status

Each book costs $15, online orders include shipping cost:
$.25 per book if <=10 books are ordered, otherwise $5 flat fee
Offline orders do not include shipping, but are taxed at 8%
Online orders arent taxed

Total cost = shipping + tax + base order price, program outputs this sum

input: books_ordered (int), order_status (int)
output: billed (float)
"""

# globals
total_revenue = 0.0  # takes sum of all orders revenue
num_online_orders = 0  # takes sum of all online orders
num_offline_orders = 0  # takes sum of all offline orders

# functions
def compute_ship_cost(order_status, books_ordered):
    global total_revenue, num_online_orders, num_offline_orders
    ship_cost = 0.0
    if order_status:
        num_online_orders += 1
        if books_ordered <= 10:
            ship_cost += books_ordered * 0.25
        else:
            ship_cost = 5.0
    return ship_cost


def compute_tax(order_status, total_price):
    global total_revenue, num_online_orders, num_offline_orders
    tax = 0.0
    tax_rate = 0.08
    if not order_status:
        num_offline_orders += 1
        tax = total_price * tax_rate
    return tax


def submit():
    global total_revenue, num_online_orders, num_offline_orders
    books_ordered = int(input("How many books have you ordered>>"))
    order_status = int(input("Is the order online or offline?(1, 0)>>"))

    price_per_book = 15.0
    total_price = books_ordered * price_per_book
    total_revenue += total_price

    ship_cost = compute_ship_cost(order_status, books_ordered)
    tax = compute_tax(order_status, total_price)
    billed = total_price + ship_cost + tax

    print(f"Billed = {billed:.2f}")


def calculate_avg_revenue():
    global total_revenue, num_online_orders, num_offline_orders
    total_orders = num_online_orders + num_offline_orders
    if total_orders > 0:
        average_revenue = total_revenue / total_orders
    else:
        average_revenue = None
    return average_revenue


def summary():
    global total_revenue, num_online_orders, num_offline_orders
    average_revenue = calculate_avg_revenue()
    
    print(f"Number of Online Orders: {num_online_orders:d}")
    print(f"Number of Offline Orders: {num_offline_orders:d}")
    
    if average_revenue is not None:
        print(f"Average Revenue: ${average_revenue:.2f}")
    else:
        print("No Data")


def reset():
    global total_revenue, num_online_orders, num_offline_orders
    total_revenue = 0.0
    num_online_orders = 0
    num_offline_orders = 0


quit = False
while not quit:
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    choice = int(input('Enter choice: '))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print("Ready for new series..")
    elif choice == 4:
        quit = True
    else:
        print('Invalid Choice!')
