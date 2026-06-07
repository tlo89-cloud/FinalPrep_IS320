"""Practice problem for A3.
In this app, the submit works correctly. Run the app and verify.
We require:
summary outputs: average price, and the number of 'big' orders,
which we define as orders with weight above 100 pounds.
compute_average_price() function provides the average price for
summary function.
reset: gets ready for a new series of outputs
code the above three functions, making updates as needed to the
code you already have.
Note the word 'pass' under the functions summary and reset below.
That is a Python technique for creating empty functions. Delete it,
and replace with the actual code for those functions.
your code *MUST* follow patterns shown in lecture 8.
remember, if you add globals, you should document them.
"""


# globals
total_price = 0.0  # sum of order prices
num_inputs = 0
num_big_orders = 0
discount_count = 0


def compute_price(wt):
    global total_price, num_inputs, num_big_orders, d
    unit_price = 5.0
    rate_discount = 0.04
    discount = 0.0
    price = unit_price * wt

    if price > 50.0:
        discount = price * rate_discount

    return price


def submit():
    global total_price, num_inputs, num_big_orders
    weight = float(input('Enter weight in lb >'))
    while weight <= 0.0 or weight > 1000.0:  # << need this in the assignment
        print(f'you entered {weight:.1f} please enter a positive value')
        weight = float(input('Enter a positive weight in lb >'))
    # weight <= 1000.0  -> reverse  -> weight > 1000.0

    is_online = int(input('Enter 1 for online order, 0 for offline'))

    while is_online not in {1, 0}:
        print(f"Input not in (1,0), please enter valid input>")
    

    # computations
    order_price = compute_price(weight)
    # inputs
    weight
    # update globals
    total_price += order_price
    num_inputs += 1
    if weight > 100.0:
        num_big_orders += 1

    print(f'Your price is: {order_price:.2f}')


def compute_average_price():
    avg_price = total_price / num_inputs
    return avg_price


def summary():
    global total_price, num_inputs, num_big_orders

    average_price = compute_average_price()
    if average_price is not None:
        print(f"Average Price: {average_price:.2f}")
    else:
        print("No orders to compute average price")
    print(num_inputs, num_big_orders)


def reset():
    global total_price, num_inputs, num_big_orders
    total_price = 0.0
    num_inputs = 0
    num_big_orders = 0


# main
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
    
    '''
    data structures
    x = 10
    y = [10, 20] list
    a = {10, 20}  set, no duplicates
    
    weight <= 0.0 or > 1000.0 

    c1 and (c2 or c3)
    '''
