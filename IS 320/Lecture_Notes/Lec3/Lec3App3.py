'''Lecture 3 App3 04.07.26 Developed by Trevor

User enters number of books ordered.
Price per book:
10$ 0-10 books (including 10)
9$ 11-100 books
8$ above 100 books
Display order price.

'''

num_ordered = int(input("Number of Books Ordered \n>>>"))

if num_ordered <= 10:
    price = 10.0
elif num_ordered <= 100:
    price = 9.0
else:
    price = 8.0

order_price = num_ordered * price

print(f"Order Price:\t{order_price:.2f}")
