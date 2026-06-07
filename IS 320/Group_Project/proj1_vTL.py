'''GROUP PROJECT SOMETHING (i forgot our number)
Team members: Henry, Hayley, Trevor, and mystery man

Project Stage: 1
Status: Complete
'''
import datetime
import random

# globals / dict. initalization

# Already filled, make at least three products with
# Attributes of products: id, name, unit price, stock (quantity available)

# Dicks Sporting Goods
products = {1001: {'name': 'Volleyball', 'unit_price': 15.00, 'stock': 500, 'in_stock': True},
            1002: {'name': 'Softball', 'unit_price': 10.00, 'stock': 100, 'in_stock': True},
            1003: {'name': 'Basketball', 'unit_price': 25.00, 'stock': 150, 'in_stock': True},
            1004: {'name': 'Football', 'unit_price': 17.00, 'stock': 450, 'in_stock': True},
            1005: {'name': 'Baseball', 'unit_price': 11.00, 'stock': 250, 'in_stock': True}
            }

# starts empty, filled as program runs
order_id = 1000
orders = {}


# functions
def display_products():
    '''Displays all available products with ID, name, and unit price
    '''
    print(f'{"ID":<10s}{"Name":<15s}{"Unit Price":<10s}')
    for pid in products:
        product_details = products[pid]
        if not product_details['in_stock']:
            continue     # in stock check, not req. here but could be useful in pt2
        name = product_details["name"]
        unit_price = product_details["unit_price"]
        print(f'{pid:<10d}{name:<15s}{unit_price:<10.2f}')


def compute_order_price(price, qty):
    '''Computes and returns the total order price
    '''
    order_price = price * qty
    return order_price


def get_date(start_date, end_date):
    '''Returns a random date between start and end date
    '''
    dates = []
    current = start_date
    while current <= end_date:
        dates.append(current)
        current += datetime.timedelta(days=1)
    random_day = random.choice(dates)
    return random_day


def print_order_details(order_id, order_dict):
    '''Prints a single order's details in label:value format
    '''
    order_date_string = order_dict['order_date'].strftime("%d-%m-%y")
    print(f'{"Order ID":<20s}:{order_id:<d}')
    print(f'{"Customer ID":<20s}:{order_dict["customer_id"]:<d}')
    print(f'{"Order Date":<20s}:{order_date_string:<15s}')
    print(f'{"Product ID":<20s}:{order_dict["product_id"]:<d}')
    print(f'{"Name":<20s}:{order_dict["product_name"]:<s}')
    print(f'{"Quantity":<20s}:{order_dict["quantity"]:<d}')
    print(f'{"Order Price":<20s}:{order_dict["order_price"]:<.2f}')


def product_id_list():
    ''' Creates a list of the current products in the dict
    '''
    prod_id_list = []
    for pid in products:
        prod_id_list.append(pid)   # check with manoj append is ok to use
    return prod_id_list


def submit_order():
    '''Handles full order submission including product selection, quantity,
    and order creation
    '''
    global products, order_id, orders
    display_products()
    print('1. Volleyball 2. Softball 3. Basketball 4. Football 5. Baseball')
    while True:
        try:
            num_choice = int(input('Choose 1, 2, 3, 4, or 5 for the product '))
            assert 1 <= num_choice <= 5
            break
        except ValueError:
            print('Product choice must be a number')
        except AssertionError:
            print('Product choice must be between 1 and 5')

    pid_list = product_id_list()
    selected_pid = pid_list[num_choice - 1]     # let me know if we find a simpler way to do this
    product_details = products[selected_pid]

    while True:
        try:
            qty_ordered = int(input('Enter quantity ordered >> '))
            assert qty_ordered > 0
            assert qty_ordered <= product_details['stock']
            break
        except ValueError:
            print('Quantity must be a number')
        except AssertionError:
            print(f"Quantity must be between 1 and {product_details['stock']:d}")

    price = product_details['unit_price']
    order_price = compute_order_price(price, qty_ordered)

    order_date = get_date(datetime.date(2021, 1, 1), datetime.date(2023, 12, 31))
    order_id += 1
    customer_id = 101   # hardcode to be updated in pt 2
    order_dict = {
        'order_date': order_date,
        'customer_id': customer_id,
        'product_id': selected_pid,
        'product_name': product_details['name'],
        'quantity': qty_ordered,
        'order_price': order_price
                }
    orders[order_id] = order_dict
    print_order_details(order_id, order_dict)


def display_orders():
    '''Displays all orders, order date is stored in the dictrionary as a date
    '''
    if not orders:
        print('No orders to display')
        return

    width = 80
    line = '-' * width
    print(line)
    print(f'|{"OrderID":^10s}|{"Customer":^10s}|{"Date":^10s}|{"Product ID":^12s}|{"Name":^10s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for oid in orders:
        order_details = orders[oid]
        customer_id = order_details['customer_id']
        date_string = order_details['order_date'].strftime("%d-%m-%y")
        prod_id = order_details['product_id']
        name = order_details['product_name']
        quantity = order_details["quantity"]
        price = order_details["order_price"]
        print(f'|{oid:<10d}|{customer_id:^10d}|{date_string:^10s}|{prod_id:^12d}|{name:^10s}|{quantity:^10d}|{price:^10.2f}|')
    print(line)


# main
# quit = False
while True:
    print('1.Submit Order 2.Display Orders 3.Exit')
    choice = int(input('Enter 1,2, or 3 >> '))
    if choice == 1:
        submit_order()
    elif choice == 2:
        display_orders()
    elif choice == 3:
        break   # will be used for logout in stage 2
    else:
        print('Invalid choice!')
print('Goodbye!')
