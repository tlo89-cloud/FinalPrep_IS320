"""  <YourName>
You do not need to define any functions.
You do not need to add any documentation.

Make a nested dictionary with the following data.

EmpID is the key. Design similar to what we did in class,
and in the HW.

EmpID  Name  Pay
2001   Jack  5000.00
2002   Jill  3000.00
2003   Joe   4000.00
2004   Jane  4500.00
2005   Jim   3500.00

"""
employees = {
    2001: {'Name': 'Jack', 'Pay': 5000.00},
    2002: {'Name': 'Jill', 'Pay': 3000.00},
    2003: {'Name': 'Joe', 'Pay': 4000.00},
    2004: {'Name': 'Jane', 'Pay': 4500.00},
    2005: {'Name': 'Jim', 'Pay': 3500.00}
    }

"""
Write a for loop to display contents of the dictionary.
Your output can look like the list above.
You do not need to worry about width, justification or lines.
"""
print('EmpID\tName\tPay')
for empid in employees:
    employee_details = employees[empid]
    name = employee_details['Name']
    pay = employee_details['Pay']
    print(f'{empid:d}\t{name:s}\t{pay:.2f}')

"""
Prompt the user to enter an employee id,
and display details of the matching employee,
display a not found message when there is no such employee.
"""
empid = int(input("Type employee id >> "))
if empid in employees:
    employee_details = employees[empid]
    name = employee_details['Name']
    pay = employee_details['Pay']
    print(f'Employee ID: {empid:d}\tName: {name:s}\tPay: {pay:.2f}')
else:
    print('Employee ID not found')

"""
Compute and print the average pay,
using a for loop to find total and count
(zero division check is not required)
"""
total_pay = 0.0
count_pay = 0
for empid in employees:
    employee_details = employees[empid]
    pay = employee_details['Pay']
    total_pay += pay
    count_pay += 1
avg_pay = total_pay / count_pay
print(f'Average Pay: ${avg_pay:.2f}')


"""
Empty out the dictionary.
"""
employees.clear()
