'''
(Adding more specs, in bold, to problem 2 from Lab 3) User specifies the number
of books ordered,  and if the order is online, or not.  You can
collect the second input by asking the user to enter 1 for online, and 0 for
offline.  You can assume that the user will enter 1 or 0 as directed. Unit
price for a  book is 15$. Online orders get shipping cost added:    per book
25 cents for less than or equal to 10 books, above that, a flat cost of  5$.
(For example, 50 books, as well as 100 books, both will have 5$ as shipping
cost) Offline orders get taxed,  at 8%. (that is: no ship cost for offline
orders, no tax for online orders)
App displays:  Order price,  inclusive of shipping/tax. (That means just 
a single result is displayed; for example, if price is 150$ and ship cost 
is 2$, what you show is 152$, and if price is 150$ and tax is 5$, what you 
show is 155$. Use a single print statement)

Use two functions: one computes shipping cost, the other 
computes tax.  Package the entire computation into a submit 
function. Call the submit a few times from the main.


'''
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


def summary():
    global total_revenue, num_online_orders, num_offline_orders
    average_revenue = total_revenue / (num_online_orders + num_offline_orders)
    print(f"Average Revenue: {average_revenue:.2f}")



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
