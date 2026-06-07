"""
Practice tasks below. No functions required.
No documentation required.

You are given the following data for orders
OrderID  Product  Quantity Price
1001     Hat      10       100.00
1002     Coat     20      1000.00
1003     Shirt     5       100.00

1.
Make a nested dictionary with these values.
OrderID is the key, and the remaining attributes are 
packaged as a dictionary. Similar design to what we
did in class for students, except you already have all the values,
and you can create the dictionary filled with values
directly.
So you simply start with
orders = {
.. type in each row here with proper syntax,
..starting with 1001: { ...., ..., ....}
}
"""
orders = {
    1001: {'Product': 'Hat', 'Quantity': 10, 'Price': 100.00},
    1002: {'Product': 'Coat', 'Quantity': 20, 'Price': 1000.00},
    1003: {'Product': 'Shirt', 'Quantity': 5, 'Price': 100.00},
        }



"""
2.
Write a for loop to display contents of the dictionary.
Your output can look like the list above.
You do not need to worry about width, justification or captions/titles/lines.
reference: display function done in class. (you don't need to write
a separate function. just a for loop.)
"""

print(f'{'OrderID':<10s}{'Product':10s}{'Quantity':<10s}{'Price':<10s}')
for oid in orders:
    order_detials = orders[oid]
    product = order_detials['Product']
    quantity = order_detials['Quantity']
    price = order_detials['Price']
    print(f'{oid:<10d}{product:10s}{quantity:<10d}{price:<10.2f}')


'''
3.
Prompt the user to enter an order id,
and display details of the matching order if it exists,
display a not found message otherwise.
reference: search by id done in class
'''
oid = int(input('Enter OrderID >>> '))

if oid not in orders:
    print('OrderID not found')

else:
    order_detials = orders[oid]
    product = order_detials['Product']
    quantity = order_detials['Quantity']
    price = order_detials['Price']
    print(f'{oid:<10d}{product:10s}{quantity:<10d}{price:<10.2f}')

'''
4.
Write a for loop to find the total of the prices,
and the count of the orders.
Compute and print the average order price
(zero division check is not required)
'''
count = 0
total_price = 0.0
for oid in orders:
    order_detials = orders[oid]
    price = order_detials['Price']
    count += 1
    total_price += price

print(f'Total Price: {total_price:.2f}')
print(f'Total Count: {count:d}')


'''
5.
Empty out the dictionary.
'''


