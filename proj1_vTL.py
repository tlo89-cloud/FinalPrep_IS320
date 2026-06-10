'''IS320 PROJECT GROUP 4 
Team members: 

Project Stage: 1
Status: Complete
'''
import datetime
import random

# globals / dict. initalization
user = None
userID = None
customer = False
manager = False
quit_program = False

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

# customer and manager dictionaries for login
customers = {101:{'name':'John', 'password':'johncustomer'},
            102:{'name':'Jane', 'password':'janecustomer'}}
managers = {201:{'name':'Bob', 'password':'bobmanager'}}


# functions

def def_correct_user_type(user_type):
    return 1 <= user_type <= 2


def login():
    global customer, manager, user, userID
    
    # --- Figure out user type --- #
    while True:
        try:
            user_type  = int(input('Choose 1 for customer, 2 for manager >\n1 OR 2 >> '))
            assert def_correct_user_type(user_type)
            break
        except ValueError:
            print('Choice must be a number')
        except AssertionError:
            print('Please choose 1 or 2')

        

        # --- Asking for User ID --- # (based on which type of user)
        
    if user_type == 1:
        user_dictionary = customers
        user = 'customer'
    else:
        user_dictionary = managers
        user = 'manager'
        
    while True:
        try:
            userID = int(input('Enter id > '))
            assert userID in user_dictionary
            break
        except ValueError:
            print('Invalid Login!')
        except AssertionError:
            print('Invalid Login!')

        # --- Ask for Passwrod --- # 
        # make sure password is in dictionary 

    while True:
        password = input('Password > ')
        if password == user_dictionary[userID]['password']:
            if user == 'customer':
                customer = True
                manager = False
                print(f'Welcome Customer {userID:d}!')
            else:
                customer = False
                manager = True
                print(f'Welcome Manager {userID:d}')
            break
        else:
            print('Incorrect password!')
#end login

        

        

               
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

def reduce_stock(pid, qty):
    '''Reduces stock when an order is placed, and updates in_stock if the item runs out'''
    product = products[pid]
    product['stock']-= qty
    if product['stock'] == 0:
        product['in_stock'] = False

def submit_order():
    '''Handles full order submission including product selection, quantity,
    and order creation
    '''
    global products, order_id, orders
    display_products()
    selected_pid = choose_product()
    product_details = products[selected_pid]

    if not product_details['in_stock']:
        print('Sorry, the selected item is out of stock.')
        return

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
    customer_id = userID   # hardcode to be updated in pt 2
    order_dict = {
        'order_date': order_date,
        'customer_id': customer_id,
        'product_id': selected_pid,
        'product_name': product_details['name'],
        'quantity': qty_ordered,
        'order_price': order_price
                }
    orders[order_id] = order_dict
    reduce_stock(selected_pid, qty_ordered)
    print_order_details(order_id, order_dict)


def customer_display_orders():
    '''Displays all orders for the current customer, order date is stored in the dictionary as a date
    '''
    if not orders:
        print('No orders to display')
        return

    width = 80
    line = '-' * width
    print(line)
    print(f'|{"OrderID":^10s}|{"Date":^10s}|{"Product ID":^12s}|{"Name":^10s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for oid in orders:
        order_details = orders[oid]
        if order_details['customer_id'] != userID:
            continue
        date_string = order_details['order_date'].strftime("%d-%m-%y")
        prod_id = order_details['product_id']
        name = order_details['product_name']
        quantity = order_details["quantity"]
        price = order_details["order_price"]
        print(f'|{oid:<10d}|{date_string:^10s}|{prod_id:^12d}|{name:^10s}|{quantity:^10d}|{price:^10.2f}|')
    print(line)

def display_orders():
    '''Displays all orders, order date is stored in the dictionary as a date
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

def manager_display_products():
    print(f'{"ID":<10s}{"Name":<15s}{"Stock":<10s}')
    for pid in products:
        product_details = products[pid]
        if not product_details['in_stock']:
            continue
        name = product_details["name"]
        stock = product_details["stock"]
        print(f'{pid:<10d}{name:<15s}{stock:<10d}')


def edit_prices():
    global products
    manager_display_products()
    selected_pid = choose_product()
    product_details = products[selected_pid]
    name = product_details['name']
    current_price = product_details['unit_price']
    print(f'The current price of {name:s} is ${current_price:.2f}.')
    while True:
        try:
            new_price = float(input('Enter the new price >>'))
            assert new_price > 0
            break
        except ValueError:
            print('Price must be a number')
        except AssertionError:
            print('Price must be greater than 0')

    product_details['unit_price'] = new_price
    print(f'The price of {name:s} has been updated to ${new_price:.2f}.')
def choose_product():
    global products
    print('1. Volleyball 2. Softball 3. Basketball 4. Football 5. Baseball')
    while True:
        try:
            num_choice = int(input('Choose 1, 2, 3, 4, or 5 for the product >>'))
            assert 1 <= num_choice <= 5
            break
        except ValueError:
            print('Product choice must be a number')
        except AssertionError:
            print('Product choice must be between 1 and 5')

    pid_list = product_id_list()
    selected_pid = pid_list[num_choice - 1]
    return selected_pid
def reorder_stock():
    global products
    selected_pid = choose_product()
    product_details = products[selected_pid]
    name = product_details['name']
    print(f'How many {name:s}s would you like to order?')
    while True:
        try:
            qty_ordered = int(input('Enter quantity ordered >> '))
            assert qty_ordered > 0
            break
        except ValueError:
            print('Quantity must be a number')
        except AssertionError:
            print(f"Quantity must be greater than 0")
    product_details['stock'] += qty_ordered
    if product_details['stock'] > 0:
        product_details['in_stock'] = True
    print(f'{qty_ordered:d} {name:s}(s) added to stock. Current stock: {product_details["stock"]:d}')



def manager_menu_valid_choice(choice):
    return 1 <= choice <= 5

def manager_menu(): 
    global  quit_program

    ''' Displays and Handles the manger menu'''
    while True:
        print('1. Display Orders    2.Edit Prices   3.Reorder Stock     4.Logout    5.Quit')
        while True:
            try:
                choice = int(input('Enter 1, 2, 3, 4, or 5 >>'))
                assert manager_menu_valid_choice(choice)
                break
            except ValueError:
                print('Choice must be a number')
            except AssertionError:
                print('Choice must be between 1 and 5 >>')

        if choice == 1:
            display_orders()
        elif choice == 2:
            edit_prices()
        elif choice == 3:
            reorder_stock()
        elif choice == 4:
            print('Logged out.')
            return
        elif choice == 5:
            quit_program = True
            return



def customer_menu_valid_choice(choice):
    return 1 <= choice <= 4

def customer_menu():
    global quit_program

    ''' Displays and handles the customer menu'''

    while True:
        print('1.Submit Order   2.Display Orders    3.Logout    4.Exit')
        while True:
            try:
                choice = int(input('1 2 or 3 >>'))
                assert customer_menu_valid_choice(choice)
                break
            except ValueError:
                print('Choice must be a number')
            except AssertionError:
                print('Choice must be between 1 and 4')

        if choice == 1:
            submit_order()
        elif choice == 2:
            customer_display_orders()  
        elif choice == 3:
            return
        elif choice == 4:
            quit_program = True
            return




        

# --- Main --- #

quit_program = False
while not quit_program:
    print('1.Login  2.Quit')
    c1 = int(input('Choose 1 or 2 >>'))
    if c1 == 1:
        login()

        if customer:
            customer_menu()
        elif manager:
            manager_menu()
    elif c1 == 2:
        break

print('Goodbye!')
