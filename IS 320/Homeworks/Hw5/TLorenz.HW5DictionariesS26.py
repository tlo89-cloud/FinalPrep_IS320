"""HW5 Trevor Lorenz 05/19/2026
"""

# globals
orders = {
    1001: {'Name': 'Alex', 'Status': 'Online', 'Price': 200.00, 'ShipCost': 20.00, 'Tax': 0.00},
    1002: {'Name': 'Adam', 'Status': 'Offline', 'Price': 300.00, 'ShipCost': 0.00, 'Tax': 15.00},
    1003: {'Name': 'Annie', 'Status': 'Offline', 'Price': 100.00, 'ShipCost': 0.00, 'Tax': 5.00},
    1004: {'Name': 'Alice', 'Status': 'Online', 'Price': 400.00, 'ShipCost': 50.00, 'Tax': 0.00},
    1005: {'Name': 'Amy', 'Status': 'Offline', 'Price': 500.00, 'ShipCost': 0.00, 'Tax': 25.00},
}

saved_filename = ''   # stores filename for repeated saves (extra credit)


# functions
def display():
    """Shows the contents of the dictionary, including a billed column.
    """
    if not orders:
        print('No data to display')
        return  # exit the function

    width = 78
    line = '-' * width
    print(line)
    print(f'|{"OrderID":^10s}|{"Name":^10s}|{"Status":^10s}|{"Price":^10s}|{"ShipCost":^10s}|{"Tax":^10s}|{"Billed":^10s}|')
    print(line)
    for oid in orders:
        order_details = orders[oid]
        name = order_details["Name"]
        status = order_details["Status"]
        price = order_details["Price"]
        ship_cost = order_details["ShipCost"]
        tax = order_details["Tax"]
        billed = price + ship_cost + tax

        print(f'|{oid:<10d}|{name:^10s}|{status:^10s}|{price:^10.2f}|{ship_cost:^10.2f}|{tax:^10.2f}|{billed:^10.2f}|')
    print(line)


def save():
    """Saves the contents of the dictionary to a text file, comma separated.
    """
    global saved_filename
    if not orders:
        print("No order data")
        return

    if saved_filename:
        filename = saved_filename
    else:
        filename = input("Type filename (excluding .txt at end) >>>")
        saved_filename = filename

    count = 0
    out_string = ''
    for oid in orders:
        order_details = orders[oid]
        name = order_details["Name"]
        status = order_details["Status"]
        price = order_details["Price"]
        ship_cost = order_details["ShipCost"]
        tax = order_details["Tax"]
        line = f'{oid:d}, {name:s}, {status:s}, {price:.2f}, {ship_cost:.2f}, {tax:.2f}'
        out_string += line + '\n'
        count += 1

    filename = f'{filename}.txt'

    with open(filename, 'w') as savefile:
        savefile.write(out_string.rstrip('\n'))
    print(f'{count:d} orders saved to {filename:s}')


def search_by_order_id():
    """Searches the contents of the dictionary for a particular order id
    and returns details
    """
    oid = int(input("Enter Order ID >>> "))
    if oid not in orders:
        print("Order ID not found")
    else:
        order_details = orders[oid]
        name = order_details["Name"]
        status = order_details["Status"]
        price = order_details["Price"]
        ship_cost = order_details["ShipCost"]
        tax = order_details["Tax"]
        billed = price + ship_cost + tax
        print(f'''
        Order ID:  {oid:d}
        Name:      {name:s}
        Status:    {status:s}
        Price:     {price:.2f}
        Ship Cost: {ship_cost:.2f}
        Tax:       {tax:.2f}
        Billed:    {billed:.2f}
                ''')


def search_by_status():
    """Searches the contents of the dictionary for a particular status
    and returns details
    """
    input_status = int(input("Enter order status (1 = Online, 0 = Offline)>>> "))
    if input_status == 1:
        search_status = 'Online'
    elif input_status == 0:
        search_status = 'Offline'
    else:
        print('Invalid input')
        search_status = ''

    if search_status:
        found = False
        out_string = ''
        for oid in orders:
            order_details = orders[oid]
            status = order_details["Status"]

            if status == search_status:
                found = True
                name = order_details["Name"]
                price = order_details["Price"]
                ship_cost = order_details["ShipCost"]
                tax = order_details["Tax"]
                billed = price + ship_cost + tax
                out_string += f'|{oid:<10d}|{name:^10s}|{status:^10s}|{price:^10.2f}|{ship_cost:^10.2f}|{tax:^10.2f}|{billed:^10.2f}|\n'

        if found:
            width = 78
            line = '-' * width
            print(line)
            print(f'|{"OrderID":^10s}|{"Name":^10s}|{"Status":^10s}|{"Price":^10s}|{"ShipCost":^10s}|{"Tax":^10s}|{"Billed":^10s}|')
            print(line)
            print(out_string.rstrip('\n'))
            print(line)
        else:
            print(f"No orders with status {search_status:s}")


def search():
    """Allows users to search through orders by either an OrderID, or by Status
    """
    quit = False
    while not quit:
        print('1. Search by Order ID  2. Search by Status 3. Done')
        choice = int(input('Enter 1,2, or 3 >>> '))
        if choice == 1:
            search_by_order_id()

        elif choice == 2:
            search_by_status()

        elif choice == 3:
            quit = True

        else:
            print("Invalid Choice")


def compute_average():
    """Returns average order price, and the offline average order price
    from the dictionary, as well as the count of orders with price above 200
    """
    offline_count = 0
    offline_total_price = 0.0
    total_count = 0
    total_price = 0.0
    price_over_200_count = 0

    for oid in orders:
        order_details = orders[oid]
        status = order_details["Status"]
        price = order_details["Price"]
        if status == 'Offline':
            offline_count += 1
            offline_total_price += price
        total_count += 1
        total_price += price
        if price > 200.00:
            price_over_200_count += 1

    if offline_count > 0:
        avg_offline_price = offline_total_price / offline_count
    else:
        avg_offline_price = None

    if total_count > 0:
        avg_price = total_price / total_count
    else:
        avg_price = None

    return avg_offline_price, avg_price, price_over_200_count


def summary():
    """Use the average function and display average price,
    offline average price and  high order count.
    """
    avg_offline_price, avg_price, price_over_200_count = compute_average()

    if avg_price is not None:
        print(f"Average price ${avg_price:.2f}")
    else:
        print("No data on  average price")

    if avg_offline_price is not None:
        print(f"Offline average price ${avg_offline_price:.2f}")
    else:
        print("No data on offline average price")

    print(f"High order count {price_over_200_count:d}")


def reset():
    """Empty out the dictionary."""
    global orders
    orders.clear()


# main
quit = False
while not quit:
    print('1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit')
    choice = int(input('Enter 1,2,3,4,5 or 6 >>'))
    if choice == 1:
        display()
    elif choice == 2:
        save()
    elif choice == 3:
        search()
    elif choice == 4:
        summary()
    elif choice == 5:
        reset()
        print('Orders reset.')
    elif choice == 6:
        quit = True
    else:
        print('Invalid choice!')
print('Goodbye!')
