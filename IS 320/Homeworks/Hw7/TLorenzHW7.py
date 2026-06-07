''' Trevor Lorenz HW7 06.04.2026

Object Oriented Programming Assignment - Hw 7

Program manages orders.
Orders have a name, quantity, online/offline status, and price.
Supports submit, load, save, display, search, summary, and reset functions.
'''

# globals
orders_list = []
saved_status = 0


# classes
class Order:
    # class variables
    total_count = 0
    online_count = 0
    offline_count = 0
    total_orders_quantity = 0.0
    total_online_quantity = 0.0
    unit_prices = {'Online': 10.0, 'Offline': 11.0}

    def __init__(self, name, quantity, online):      # self represents the object itself (e.g. taxpayer)
        self.name = name    # create an attribute 'name' for self
        self.quantity = quantity
        self.online = online
        if online == 1:
            self.mode = 'Online'
            Order.online_count += 1
            Order.total_online_quantity += quantity
        else:
            self.mode = 'Offline'
            Order.offline_count += 1
        Order.total_count += 1
        Order.total_orders_quantity += quantity
        self.price = self.compute_price()

    def compute_price(self):
        unit_price = Order.unit_prices[self.mode]
        price = unit_price * self.quantity
        return price

    def __str__(self):      # every function in classes must have first paramater be self
        '''must return string. supports the print. '''
        return f'''
        Name\t\t:{self.name:s}
        Quantity\t:{self.quantity:d}
        Online\t\t:{self.mode:s}
        Price\t\t:{self.price:.2f}

        '''

    def display_line(self):
        return f'|{self.name:<10s}|{self.quantity:<10d}|{self.mode:<10s}|{self.price:<10.2f}'

    def csv_line(self):
        return f'{self.name:s},{self.quantity:d},{self.online:d}'

    def matches_name(self, name_in):
        return self.name.upper() == name_in.upper()

    def matches_status(self, status_in):
        return self.online == status_in

    @staticmethod
    def header():
        return f'|{'Name':<10s}|{'Quantity':^10s}|{'Mode':^10s}|{'Price':^10s}|'

    @staticmethod
    def divider():
        width = 45
        return '-' * width

    # class methods
    @classmethod
    def compute_average(cls):
        if cls.total_count > 0:
            avg = cls.total_orders_quantity / cls.total_count
        else:
            avg = None

        if cls.online_count > 0:
            online_avg = cls.total_online_quantity / cls.online_count
        else:
            online_avg = None

        return avg, online_avg

    @classmethod
    def report_summary(cls):
        avg, online_avg = cls.compute_average()
        report = ''
        # add lines to report
        report += f'\nTotal order count: {cls.total_count:d}'
        report += f'\nOnline order count: {cls.online_count:d}'
        report += f'\nOffline order count: {cls.offline_count:d}'

        if avg is not None:
            report += f'\nAverage order quantity {avg:.2f}'
        else:
            report += '\nNo data for average'
        if online_avg is not None:
            report += f'\nAverage online order quantity {online_avg:.2f}'
        else:
            report += '\nNo data for average'
        return report

    @classmethod
    def reset_data(cls):
        cls.total_count = 0
        cls.online_count = 0
        cls.offline_count = 0
        cls.total_orders_quantity = 0.0
        cls.total_online_quantity = 0.0

# functions


def process_line(ln_in, sep=None):
    '''Parses input line, creates an Order object, appends to list, returns object.'''
    global saved_status
    list_in = ln_in.split(sep)

    name = list_in[0]
    quantity = int(list_in[1])
    online = int(list_in[2])
    # 1 make a taxpayer object
    order = Order(name, quantity, online)
    # 2 add it to the global list
    orders_list.append(order)
    saved_status = 0
    return order


def submit():
    '''Reads a line of input from user, processes it, and prints the order.'''
    line_in = input('Enter name, quantity, and online (1) or offline (0)')
    order = process_line(line_in)
    print(order)


def display():
    '''Prints all orders in the list as a formatted table.'''
    global orders_list

    if not orders_list:
        print('No data to display')
        return

    print(Order.divider())
    print(Order.header())
    print(Order.divider())

    for order in orders_list:
        row = order.display_line()
        print(row)


def save():
    '''Saves all orders to a user-specified file in csv format.'''
    global orders_list, saved_status
    if orders_list:
        out_data = ''
        count = 0
        for order in orders_list:
            line = order.csv_line()
            out_data += line+'\n'
            count += 1
        saved_outfile = input('Please input outfile name >> ')
        with open(saved_outfile, 'w') as outfile:
            outfile.write(out_data.rstrip('\n'))
        saved_status = 1

        print(f'{count:d} orders saved to {saved_outfile:s} ')
    else:
        print("No data to save")


def load():
    '''Loads orders from in.txt and appends them to the orders list.'''
    global orders_list
    infile = 'in.txt' 
    sep = ','
    count = 0
    with open(infile, 'r') as loadfile:
        for line in loadfile:
            process_line(line, sep)
            count += 1
    print(f'{count:d} orders loaded from {infile:s}')           


def summary():
    '''Prints a summary report of order counts and averages.'''
    global orders_list
    report = Order.report_summary()
    print(report)


def reset():
    '''Clears all order data and resets class variables.'''
    global orders_list, saved_status
    if saved_status == 0 and orders_list:
        print('Data has not been saved. Would you like to save first?')
        choice = int(input('1: Yes save, 0: Dont save >>> '))
        if choice == 1:
            save()    
    clear_data()    # clear out data structure
    Order.reset_data()       # clear out data model
    print('All data reset..')


def clear_data():
    '''Clears the global orders list.'''
    global orders_list
    orders_list.clear()


def search():
    '''Searches orders by name or status and prints matching results.'''
    global orders_list, saved_status
    status = False
    if not orders_list:
        print('No data to search')
        status = True

    while status == False:
        search_type = int(input('Type 1 to search by name and 2 to search by status'))

        if search_type == 1:
            name_in = input('Type name >> ')
            found = False
            for order in orders_list:
                if order.matches_name(name_in):
                    found = True
                    print(order)
            if not found:
                print(f'{name_in:s} not found in orders')
            status = True

        elif search_type == 2:
            status_in = int(input('Type order status >> '))
            found = False
            for order in orders_list:
                if order.matches_status(status_in):
                    found = True
                    print(order)
            if not found:
                print(f'{status_in:d} not found in orders')
            status = True

        else:
            print('Please type 1 or 2')


# main
quit = False

while not quit:

    print('1.Submit 2.Load 3.Summary 4.Display 5.Save 6.Search 7.Reset 8.Exit')
    choice = int(input('Enter choice:  '))
    if choice == 1:
        submit()
    elif choice == 2:
        load()
    elif choice == 3:
        summary()
    elif choice == 4:
        display()
    elif choice == 5:
        save()
    elif choice == 6:
        search()
    elif choice == 7:
        reset()
    elif choice == 8:
        if saved_status == 0 and orders_list:
            print('Data has not been saved. Would you like to save first?')
            choice = int(input('1: Yes save, 0: Dont save >>> '))
            if choice == 1:
                save()
        quit = True

    else:
        print('Invalid Choice!')
