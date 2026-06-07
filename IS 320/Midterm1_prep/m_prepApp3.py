'''
Problem 3


Salesperson-Commission problem from earlier - lab 2
User enters sales (a dollar amount)

Sales:  At or above 2000.0 gets commission at 5%. Base pay is 250, and pay is base pay plus commission.
Compute commission using a function.

Submit displays  pay. Commission displayed if there is commission; no message displayed for No Commission   
(same specifications as the original lab problem)    (pay includes base pay and commission, if any)

Summary displays Average Commission, Average Pay, Count of Commission Earners : Use functions for the averages.
Reset gets ready for new series of inputs
Extras: 

Validate sales as being positive


Similar to the above three problems, use other lab problems to build a submit/summary/reset structure.  

In each problem, try to do:
Multiple averages 
Multiple counts
Validation of selected inputs
Submit printing multiple result variables returned by a single function

Make sure to also:
  Abbreviate if statements such as if married == 1: to if married:    
Consult the multiple-if.py on Canvas
Your if statements will need to be optimal for full points
'''

# globals
count_commission = 0
total_commission = 0.0
count_pay = 0
total_pay = 0.0


# functions
def calc_commission(sales):
    global count_commission, total_commission, count_pay, total_pay
    commission = 0.0
    if sales >= 2000.0:
        commission = sales * 0.05
    return commission


def submit():
    global count_commission, total_commission, count_pay, total_pay
    sales = int(input("input sales >> "))
    while sales < 0:
        print(f"You input {sales:.2f}, please input a positive number")
        sales = int(input("input POSITIVE sales >> "))

    base_pay = 250.0
    commission = calc_commission(sales)
    if commission > 0:
        print(f"Your Commission is: {commission:.2f}")
        total_commission += commission
        count_commission += 1
    pay = base_pay + commission
    count_pay += 1
    total_pay += pay
    print(f"Total Pay: {pay:.2f}")


def calc_average_commission():
    global count_commission, total_commission, count_pay, total_pay
    if count_commission > 0:
        avg = total_commission / count_commission
    else:
        avg = None
    return avg

def calc_average_pay():
    global count_commission, total_commission, count_pay, total_pay
    if count_pay > 0:
        avg = total_pay / count_pay
    else:
        avg = None
    return avg

def summary():
    global count_commission, total_commission, count_pay, total_pay
    avg_commission = calc_average_commission()
    avg_pay = calc_average_pay()
    count_of_comm_earners = count_commission
    if avg_commission is None:
        print("No data available on avg comm")
    else:
        print(f"Average Commission: {avg_commission:.2f}")
    print(f"Count of commission earners: {count_of_comm_earners:d}")

    if avg_pay is None:
        print("No Data Availbale on avg pay")
    else:
        print(f"Average Pay: {avg_pay:.2f}")



def reset():
    global count_commission, total_commission, count_pay, total_pay
    count_commission = 0
    total_commission = 0.0
    count_pay = 0
    total_pay = 0.0
    print("Ready for new data!")


quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset. 4.Exit')
   print('Choose 1,2,3, or 4')
   choice = int(input('>>'))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       quit = True
   else:
       print('Invalid choice! Choose 1,2,3, or 4')
print('Bye!')















'''
# globals
total_commission = 0.0
commission_count = 0
total_pay = 0.0
pay_count = 0


# funcitons

def compute_commission(sales):
    global total_commission, commission_count, total_pay, pay_count
    commission = 0.0
    base_pay = 250.0
    if sales >= 2000.0:
        commission = sales * 0.05
        commission_count += 1
    pay = base_pay + commission
    total_commission += commission
    pay_count += 1
    return pay, commission

# is there another way to do this except for this right here ^^

def submit():
    global total_commission, commission_count, total_pay, pay_count
    sales = float(input("Please input sales >>> "))

    pay, commission = compute_commission(sales)
    if commission > 0:
        print(f"Commission: {commission:.2f}")
    print(f"Total pay: {pay:.2f}")


def calc_average_commission():
    global total_commission, commission_count, total_pay, pay_count
    if commission_count == 0:
        return None
    else:
        avg = total_commission / commission_count
    return avg


def calc_average_pay():
    global total_commission, commission_count, total_pay, pay_count
    if pay_count == 0:
        return None
    else:
        avg = total_pay / pay_count
    return avg


def summary():
    global total_commission, commission_count, total_pay, pay_count
    avg_comm = calc_average_commission()
    avg_pay = calc_average_pay()
    print(f"average commission: {avg_comm}")
    print(f"average pay: {avg_pay}")



def reset():
    global total_commission, commission_count, total_pay, pay_count
    total_commission = 0.0
    commission_count = 0
    total_pay = 0.0
    pay_count = 0
    print("Ready for more data!")


quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset. 4.Exit')
   print('Choose 1,2,3, or 4')
   choice = int(input('>>'))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       quit = True
   else:
       print('Invalid choice! Choose 1,2,3, or 4')
print('Bye!')
'''