'''IS320 PROJECT GROUP 4
Team members:

Project Stage: 2
Status: Complete
'''
import datetime
import random

#globals
user = None #current user ('customer' or 'manager')
userID = None #current user's id (int)
quit_program = False #flag to control main loop, set to True when user chooses to quit

# Dick's Sporting Goods
# Attributes of products: id (key), name, unit price, stock (quantity available)

products = {1001: {'name': 'Volleyball', 'unit_price': 15.00, 'stock': 500},
            1002: {'name': 'Softball', 'unit_price': 10.00, 'stock': 100},
            1003: {'name': 'Basketball', 'unit_price': 25.00, 'stock': 150},
            1004: {'name': 'Football', 'unit_price': 17.00, 'stock': 450},
            1005: {'name': 'Baseball', 'unit_price': 11.00, 'stock': 250}
            }


order_id = 10000
orders = {}

# customer and manager dictionaries for login
customers = {101: {'name': 'John', 'password': 'johncustomer'},
             102: {'name': 'Jane', 'password': 'janecustomer'}}
managers = {201: {'name': 'Bob', 'password': 'bobmanager'}}



def comp_price(product, quantity):
    return product['unit_price'] * quantity


def get_date():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return start_date + datetime.timedelta(days=random_days)


def in_stock(product):
    return product['stock'] > 0


def can_meet_order_of(product, quantity):
    return 0 < quantity <= product['stock']


def update_stock(product, quantity):
    product['stock'] += quantity


def print_order(order_id):
    order_dict = orders[order_id]
    order_date_string = order_dict['order_date'].strftime('%d-%m-%y')
    print(f'{"Order ID":<20s}:{order_id:<d}')
    print(f'{"Customer ID":<20s}:{order_dict["customer_id"]:<d}')
    print(f'{"Order Date":<20s}:{order_date_string:<15s}')
    print(f'{"Product ID":<20s}:{order_dict["product_id"]:<d}')
    print(f'{"Name":<20s}:{order_dict["product_name"]:<s}')
    print(f'{"Quantity":<20s}:{order_dict["quantity"]:<d}')
    print(f'{"Order Price":<20s}:{order_dict["order_price"]:<.2f}')


#login

def valid_user_type(user_type):
    return 1 <= user_type <= 2


def login():
    global user, userID

    while True:
        try:
            user_type = int(input('Choose 1 for customer, 2 for manager >\n1 OR 2 >> '))
            assert valid_user_type(user_type)
            break
        except ValueError:
            print('Choice must be a number')
        except AssertionError:
            print('Please choose 1 or 2')

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

    while True:
        password = input('Password > ')
        if password == user_dictionary[userID]['password']:
            if user == 'customer':
                print(f'Welcome Customer {userID:d}!')
            else:
                print(f'Welcome Manager {userID:d}!')
            break
        else:
            print('Incorrect password!')


#product display/selection

def display_products():
    '''Displays available products with ID, name, and unit price (customer view)'''
    print(f'{"ID":<10s}{"Name":<15s}{"Unit Price":<10s}')
    for pid in products:
        product = products[pid]
        if not in_stock(product):
            continue   # customers only see items that can actually be ordered
        print(f'{pid:<10d}{product["name"]:<15s}{product["unit_price"]:<10.2f}')


def manager_display_products():
    '''Displays ALL products with complete information (manager view).
    Out-of-stock items are included -- the manager needs to see them
    to reorder stock.'''
    print(f'{"ID":<10s}{"Name":<15s}{"Unit Price":<12s}{"Stock":<10s}')
    for pid in products:
        product = products[pid]
        print(f'{pid:<10d}{product["name"]:<15s}{product["unit_price"]:<12.2f}{product["stock"]:<10d}')


def choose_product():
    '''Prompts the user to select a product, validating the selection.
    Builds an explicit mapping of menu number -> product id
    (1:1001, 2:1002, ...) from the products dictionary, so the menu and
    the selection can never fall out of sync, and both stay correct if
    products are ever added or changed.'''
    pid_list = list(products.keys())
    choice_map = {}
    menu_line = ''
    choice_num = 1
    for pid in pid_list:
        choice_map[choice_num] = pid
        menu_line += f'{choice_num:d}. {products[pid]["name"]:s}  '
        choice_num += 1
    num_products = len(choice_map)

    print(menu_line)
    while True:
        try:
            num_choice = int(input(f'Choose 1 - {num_products:d} for the product >> '))
            assert num_choice in choice_map
            break
        except ValueError:
            print('Product choice must be a number')
        except AssertionError:
            print(f'Product choice must be between 1 and {num_products:d}')

    return choice_map[num_choice]


#customer functions

def submit():

    global order_id

    display_products()
    selected_pid = choose_product()
    product = products[selected_pid]

    if not in_stock(product):
        print('Sorry, the selected item is out of stock.')
        return

    while True:
        try:
            qty_ordered = int(input('Enter quantity ordered >> '))
            assert can_meet_order_of(product, qty_ordered)
            break
        except ValueError:
            print('Quantity must be a number')
        except AssertionError:
            print(f'Quantity must be between 1 and {product["stock"]:d}')

    order_price = comp_price(product, qty_ordered)
    order_date = get_date()

    order_id += 1   # first order gets id 10001
    orders[order_id] = {
        'order_date': order_date,
        'customer_id': userID,
        'product_id': selected_pid,
        'product_name': product['name'],
        'quantity': qty_ordered,
        'order_price': order_price
    }
    update_stock(product, -qty_ordered)
    print_order(order_id)


def customer_display_orders():
    found = False
    width = 70
    line = '-' * width
    print(line)
    print(f'|{"OrderID":^10s}|{"Date":^10s}|{"Product ID":^12s}|{"Name":^12s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for oid in orders:
        order = orders[oid]
        if order['customer_id'] != userID:
            continue
        found = True
        date_string = order['order_date'].strftime('%d-%m-%y')
        print(f'|{oid:<10d}|{date_string:^10s}|{order["product_id"]:^12d}|'
              f'{order["product_name"]:^12s}|{order["quantity"]:^10d}|{order["order_price"]:^10.2f}|')
    print(line)
    if not found:
        print('No orders to display')


#manager functions

def manager_display_orders():
    if not orders:
        print('No orders to display')
        return

    width = 81
    line = '-' * width
    print(line)
    print(f'|{"OrderID":^10s}|{"Customer":^10s}|{"Date":^10s}|{"Product ID":^12s}|{"Name":^12s}|{"Quantity":^10s}|{"Price":^10s}|')
    print(line)
    for oid in orders:
        order = orders[oid]
        date_string = order['order_date'].strftime('%d-%m-%y')
        print(f'|{oid:<10d}|{order["customer_id"]:^10d}|{date_string:^10s}|{order["product_id"]:^12d}|'
              f'{order["product_name"]:^12s}|{order["quantity"]:^10d}|{order["order_price"]:^10.2f}|')
    print(line)


def edit_prices():
    '''Manager edits unit price for an individual product. Products are
    displayed (complete information) before and after the edit, per spec.'''
    manager_display_products()
    selected_pid = choose_product()
    product = products[selected_pid]
    print(f'The current price of {product["name"]:s} is ${product["unit_price"]:.2f}.')

    while True:
        try:
            new_price = float(input('Enter the new price >> '))
            assert new_price > 0
            break
        except ValueError:
            print('Price must be a number')
        except AssertionError:
            print('Price must be greater than 0')

    product['unit_price'] = new_price
    print(f'The price of {product["name"]:s} has been updated to ${new_price:.2f}.')
    manager_display_products()


def reorder_stock():
    '''Manager chooses a product and specifies a reorder quantity, which is
    added to the current stock. Products are displayed first so the manager
    can see current stock levels (including items at 0).'''
    manager_display_products()
    selected_pid = choose_product()
    product = products[selected_pid]
    print(f'How many {product["name"]:s}s would you like to order?')

    while True:
        try:
            qty_ordered = int(input('Enter quantity ordered >> '))
            assert qty_ordered > 0
            break
        except ValueError:
            print('Quantity must be a number')
        except AssertionError:
            print('Quantity must be greater than 0')

    update_stock(product, qty_ordered)
    print(f'{qty_ordered:d} {product["name"]:s}(s) added to stock. '
          f'Current stock: {product["stock"]:d}')


#menu functions
def manager_menu_valid_choice(choice):
    return 1 <= choice <= 5


def manager_menu():
    '''Displays and handles the manager menu'''
    global quit_program

    while True:
        print('1. Display Orders   2. Edit Prices   3. Reorder Stock   4. Logout   5. Quit')
        while True:
            try:
                choice = int(input('Enter 1, 2, 3, 4, or 5 >> '))
                assert manager_menu_valid_choice(choice)
                break
            except ValueError:
                print('Choice must be a number')
            except AssertionError:
                print('Choice must be between 1 and 5')

        if choice == 1:
            manager_display_orders()
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
    '''Displays and handles the customer menu.
    Option 3 logs out (program keeps running), Option 4 quits.'''
    global quit_program

    while True:
        print('1. Submit Order   2. Display Orders   3. Logout   4. Quit')
        while True:
            try:
                choice = int(input('Enter 1, 2, 3, or 4 >> '))
                assert customer_menu_valid_choice(choice)
                break
            except ValueError:
                print('Choice must be a number')
            except AssertionError:
                print('Choice must be between 1 and 4')

        if choice == 1:
            submit()
        elif choice == 2:
            customer_display_orders()
        elif choice == 3:
            print('Logged out.')
            return
        elif choice == 4:
            quit_program = True
            return


#main
quit_program = False
while not quit_program:
    print('1. Login   2. Quit')
    try:
        c1 = int(input('Choose 1 or 2 >> '))
        assert 1 <= c1 <= 2
    except (ValueError, AssertionError):
        print('Please choose 1 or 2')
        continue

    if c1 == 1:
        login()
        if user == 'customer':
            customer_menu()
        elif user == 'manager':
            manager_menu()
    else:
        break

print('Goodbye!')
