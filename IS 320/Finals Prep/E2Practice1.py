#The tasks below directly replicate what we did in class,
#skipping the more time consuming submit and load.
#There is no additional problem solving or tricky features
#involved.  
#If you are familiar with what we did with oop in class,
#the time taken should be just the time to type up the code.

#hint: if you need to generate a multi-line string with formatting,
#use f''' .....'''  instead of f'...' and type the lines exactly as
#you would like to see them displayed.  Avoid triple double quotes, however.

class Employee:
    # class globals
    total_hours = 0.0
    hours_count = 0
    total_hourly_pay = 0.0
    hourly_pay_count = 0

    def __init__(self, name, hours, hourly, pay):
        self.name = name
        self.hours = hours
        self.hourly = hourly
        self.pay = pay
        if hourly == 1:
            self.status = 'Hourly'
            Employee.hourly_pay_count += 1
            Employee.total_hourly_pay += pay
        else:
            self.status = 'Salaried'
        Employee.total_hours += hours
        Employee.hours_count += 1

    def __str__(self):
        '''must return string. supports the print. '''
        return f'''
        Name:\t{self.name:s}
        Hours:\t{self.hours:d}
        Status:\t{self.status:s}
        Pay:\t{self.pay:.2f}

        '''

    def display_line(self):
        return f'|{self.name:<10s}|{self.hours:^10d}|{self.status:^10s}|{self.pay:>10.2f}|'

    def csv_line(self):
        return f'{self.name:s},{self.hours:d},{self.status:s},{self.pay:.2f}'

    def matches_name(self, name_in):
        return self.name.upper() == name_in.upper()

    @staticmethod
    def header():
        return f'|{'Name':^10s}|{'Hours':^10s}|{'Status':^10s}|{'Pay':^10s}|'

    @staticmethod
    def divider():
        width = 45
        return '-' * width

    # classmethods
    @classmethod
    def compute_average(cls):
        if cls.total_hours > 0:
            hour_avg = cls.total_hours / cls.hours_count
        else:
            hour_avg = None

        if cls.hourly_pay_count > 0:
            hourly_avg_pay = cls.total_hourly_pay / cls.hourly_pay_count
        else:
            hourly_avg_pay = None

        return hour_avg, hourly_avg_pay

    @classmethod
    def report_summary(cls):
        hour_avg, hourly_avg_pay = cls.compute_average()
        report = ''
        # add lines to report
        report += f'\nTotal hours count: {cls.hours_count:d}'
        report += f'\nOnline hourly pay count: {cls.hourly_pay_count:d}'

        if hour_avg is not None:
            report += f'\nAverage hours {hour_avg:.2f}'
        else:
            report += '\nNo data for average'
        if hourly_avg_pay is not None:
            report += f'\nAverage pay for hourly workers {hourly_avg_pay:.2f}'
        else:
            report += '\nNo data for average'
        return report

    @classmethod
    def reset_data(cls):
        cls.total_hours = 0.0
        cls.hours_count = 0
        cls.total_hourly_pay = 0.0
        cls.hourly_pay_count = 0

#Add code to the class to make the code below work.
#the inputs are  name, hours(int), hourly(1/0), pay
#the init will store these, and add a status attribute
#status is Hourly or Salaried, when hourly is 1 or 0 respectively.
#no other computations.

employees = [

    Employee('Alex', 10, 1, 150.00),
    Employee('Ben', 20, 0, 500.00),
    Employee('Cathy', 10, 0,  250.00),
    Employee('Denise', 30, 1, 450.00),
    Employee('Emily', 50, 0, 1250.00),
    Employee('Frank', 40, 1, 600.00),
    Employee('Ben', 20, 1, 300.00),

]

#Add code to the class,
#and then add code here, to produce the following
#display outputs (ignore the last Ben missing in
# output below.)
#The code you add here is what you would normally
#place inside a display function. There is no need to
#make a function.
#The line and caption should be generated using techniques
#shown in class.

print(Employee.divider())
print(Employee.header())
print(Employee.divider())
for employee in employees:
    print(employee.display_line())


"""
---------------------------------------------
|   Name   |  Hours   |  Status  |   Pay    |
---------------------------------------------
|Alex      |    10    |  Hourly  |    150.00|
|Ben       |    20    | Salaried |    500.00|
|Cathy     |    10    | Salaried |    250.00|
|Denise    |    30    |  Hourly  |    450.00|
|Emily     |    50    | Salaried |   1250.00|
|Frank     |    40    |  Hourly  |    600.00|
---------------------------------------------
"""

#key = input('Enter Name to Search For > ')
#Add code here to find and print the employee 
#matching the name typed in by user.
#There are three sample outputs provided below.


name_in = input('Enter Name to Search For > ')

found = False
for employee in employees:
    if employee.matches_name(name_in):
        found = True
        print(employee)
if not found:
    print(f'{name_in:s} not found in orders')


"""
Enter Name to Search For > Frank

        Name:   Frank
        Hours:  40
        Status: Hourly
        Pay:    600.00 

Enter Name to Search For > Charles
Not found

Enter Name to Search For > Ben

        Name:   Ben
        Hours:  20
        Status: Salaried
        Pay:    500.00

        Name:   Ben
        Hours:  20
        Status: Hourly
        Pay:    300.00
"""

#Add code here to save the contents of the employees list
#as a comma separated text file.
#Save file contents:


if employees:
    out_data = ''
    for employee in employees:
        line = employee.csv_line()
        out_data += line+'\n'
    saved_outfile = input('Please input outfile name >> ')
    with open(saved_outfile, 'w') as outfile:
        outfile.write(out_data.rstrip('\n'))
    print('orders saved')
else:
    print("No data to save")
"""
Alex,10,Hourly,150.00
Ben,20,Salaried,500.00
Cathy,10,Salaried,250.00
Denise,30,Hourly,450.00
Emily,50,Salaried,1250.00
Frank,40,Hourly,600.00
Ben,20,Hourly,300.00
"""

#Add necessary code to the class
#to generate the summary information as below.
#There are two sets of outputs below.
#After the first set, the data was reset,
#And the summary info was printed again.
#You need to do the same as well.
#(i.e. show the summary,  reset everything, show the
# summary again)
#The summary info is prepared inside the class
#With a single line of code below calling a
#method inside the class to print out the info generated.a

#
print(Employee.report_summary())
Employee.reset_data()
print(Employee.report_summary())
"""
Average Hours:25.71
Total Pay for Hourly Employees: 1500.00
No data to compute average with
Total Pay for Hourly Employees: 0.00
"""








