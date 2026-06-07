"""
This global dictionary contains order id:order price pairs.

"""

orders = {
    1001:150.00,
    1002:250.00,
    1003:300.00,
    1004:200.00,
    1005:100.00
}
#functiions
def display():
    """Show the contents of the dictionary."""
    if not orders:
        print('No data to display')
        return #exit the function
    
    width = 28
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^10s}|{"Order Price":^15s}|')
    print(line)
    for oid in orders:
        price = orders[oid]
        print(f'|{oid:<10d}|{price:>15.2f}|')
    print(line)


def save():
    """Save the contents of the dictionary to a text file, comma separated."""
    if not orders:
        print('No data to save.')
        return #exit the function
    
    out_string = ''
    for oid in orders:
        price = orders[oid]
        line = f'{oid:d},{price:.2f}'
        out_string += line + '\n'

    
    with open('dictionary1.txt', 'w') as savefile: # savefile = open(...)
        savefile.write(out_string.rstrip('\n'))

    print('Data saved.')

def search():
    """Search for the price matching order id entered by the user."""
    if not orders:
        print('No data to search in')
        return #exit the function

    oid = int(input('Enter order ID >>'))
    if oid in orders:
        price = orders[oid]
        print(oid, price)
    else:
        print('Not ppresent.')

def compute_average():
    """Return average order price from the dictionary.

    Also return the count of orders with price above 200.00
    """
    global orders
    total_price = 0.0
    order_count = 0
    high_count = 0

    for order_id in orders:
        price = orders[order_id]
        #update totals
        total_price += price
        order_count += 1
        if price > 200.0:
            high_count += 1
    #end for loop

    if order_count > 0:
        avg = total_price / order_count
    else:
        avg = None
    return avg, high_count

def summary():
    """Use the average function and display average price, and high order count."""
    average_price, high_count = compute_average()
    if average_price is not None:
        print(average_price)
    else:
        print('No data to compute average.')
    print(high_count)

def reset():
    """Empty out the dictionary."""
    global orders
    orders.clear()




#main
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
        print('Data has been reset.')
    elif choice == 6:
        quit = True
    else:
        print('Invalid choice!')
print('Goodbye!')

"""
Results of running the program:

1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>1
-----------------------
|    ID    |  Price   |
-----------------------
|1001      |    150.00|
|1002      |    250.00|
|1003      |    300.00|
|1004      |    200.00|
|1005      |    100.00|
-----------------------
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>2
Data saved to dlab1.txt.      <<- Contents of saved file -scroll to end.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>3
Enter order ID to search for >>1004

        Order ID        :1004
        Order Price     :200.00
        
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>3
Enter order ID to search for >>1010
No order with ID 1010.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>4

        Average Price           :200.00
        High Order Count        :2
        
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>5
Orders reset.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>1
No orders to display.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>2
No orders to save.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>3
No orders to search in.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>4
No orders for average and count.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>6
Goodbye!

Contents of saved file:
1001,150.00
1002,250.00
1003,300.00
1004,200.00
1005,100.00
"""
