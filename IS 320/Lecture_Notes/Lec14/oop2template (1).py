# -----
# an object is a variable.
# object = attributes (variables) + methods (functions)
# taxpayer object contains: name,income,tax  + methods like compute_tax()
# -------
"""
    -------
    you can start by thinking of a class as a container of multiple
    functions, which are copied into each object.

    'method' = function, inside class.
    in Python, two special methods  __init__()   and __str__() in classes.

    'instance' means instance of the class = object. 
    -------
    
    Instance attributes: (attributes of object):name,income, tax
    Instance methods: init, str, display_line,?

    Class attributes: total_tax, count
    Class methods: ?

    """

"""
instance methods:  
inside a class   self.do_something() 
outside a class  taxpayer.do_something()

instance variables:   self.name    taxpayer.name


NOTES on class methods:
'class can only see class'
class methods work *only* with class members
class methods work with class methods and variables, ONLY

belong to the class Taxpayer.
inside a class method,  cls.count  cls.do_something()
outside a class method,  Taxpayer.count  Taxpayer.do_something()


"""

# globals
taxpayerlist = [] # global list to store taxpayer objects



# classes
class Taxpayer:  #blueprint for making taxpayer objects
    #class variables
    count = 0
    total_tax = 0.0
    count_high = 0
    cutoffs = {'WA': 1000000.0, 'OR': 70000}

    def __init__(self, name, income, state):  # constructor. creates new taxpayer object.
        self.name = name
        self.income = income
        self.state = state.upper()
        self.tax = self.compute_tax()   # -> compute_tax(self)
        # update totals
        Taxpayer.count += 1
        Taxpayer.total_tax += self.tax

    def compute_tax(self):
        cutoff = Taxpayer.cutoffs[self.state]
        if self.income < cutoff:
            rate = 0.1
        else:
            rate = 0.15
            Taxpayer.count_high += 1
        return self.income * rate

    def __str__(self):  # returns string version of object. used by print()
        return f'''
        Name\t:{self.name:s}
        Income\t:{self.income:.2f}
        Tax\t:{self.tax:.2f}
        '''

    def display_line(self):
        return f'|{self.name:<10s}|{self.income:>10.2f}|{self.tax:>10.2f}|{self.state:^10s}|'

    def csv_line(self):
        pass

    def matches_name(self, name_in):
        return self.name.upper() == name_in.upper()

    # class methods
    @classmethod
    def compute_average(cls):
        if cls.count > 0:
            avg = cls.total_tax / cls.count
            # id cls.count_high is > etc.
        else:
            avg = None
            # avg_high = None
        return avg

    @classmethod    # nessecary here <<<
    def report_summary(cls):   # stand in for class
        average_tax = cls.compute_average()
        report = ''
        # add lines to report
        report += f'\nTaxpayer count: {cls.count:d}'
        report += f'\nHigh income count: {cls.count_high:d}'
        if average_tax is not None:
            report += f'Average Tax {average_tax:.2f}'
        else:
            report += 'No data for average'
        return report

    @classmethod
    def reset_data(cls):
        cls.count = 0
        cls.count_high = 0
        cls.total_tax = 0

    # helper functions for headers and dividers
    @staticmethod
    def header():
        return f'|{'Name':<10s}|{'Income':^10s}|{'Tax':^10s}|'

    @staticmethod   # neither self, nor class is needed.    classname.staticmethod()
    def divider():
        width = 34
        return '-' * width


# end class


# functions
def process_line(line_in, sep=None):
    # process the line to make and store the object
    list_in = line_in.strip().split(sep)  # .split(sep) = sep delimited inputs
    name = list_in[0]
    income = float(list_in[1])
    state = list_in[2]
    # create a Taxpayer object
    taxpayer = Taxpayer(name, income, state)
    # 0. an obj is created -> self     self, name, income
    # 1. attributes for the object are created by init.    self.name = name
    # 2. 'taxpayer' is set to be equal to self.

    # store that in the global list
    taxpayerlist.append(taxpayer)
    return taxpayer


def submit():
    line_in = input('Enter name and income and state >>')
    taxpayer = process_line(line_in)
    print(taxpayer)  # is same as print(taxpayer.__str__())


"""
pre-requisite for load and save:
 Settings: search for Execute in File Dir, check the box.

pre-requisite for load:
make a text file, preferably using VS Code, named same as infile below, in
the same folder as this .py file, with contents like below (copy and paste)
Alex,100000
Ben,200000
Cathy,10000
Denise,300000
Emily,150000
Make *absolutely sure* to have no empty lines in the file,
and to *save* the file  (use File-Save or CMD/Control S)
"""

def load():
    global taxpayerlist
    infile = 'in.txt' 
    sep = ','
    with open(infile, 'r') as loadfile:
        for line in loadfile:
            process_line(line, sep)
            # process the line to create a taxpayer object
            # and store the object in the global list


def display():
    global taxpayerlist

    if not taxpayerlist:
        print('No data to display')     # needs to be added to anyhting accesign the list
        return
    print(Taxpayer.divider())
    print(Taxpayer.header())
    print(Taxpayer.divider())

    for taxpayer in taxpayerlist:
        # get a table row for the taxpayer
        # print it
        row = taxpayer.display_line()   # inside the class we say self.function() and outside we use what we assigned the class to (taxpayer) outside the class
        print(row)


def summary():
    '''display count, high_count, average_tax, high_tax'''
    report = Taxpayer.report_summary()
    print(report)


def save():
    """Save contents of the list to a text file in csv format,
    with lines like  Alex,10000.00,1000.00  for name,income,tax"""

    global taxpayerlist

    '''
    0.Initialize a master string
    1.Get a csv string name,income,tax for each taxpayer in the list
    2.append it to the master string
    3.Open a file, and write the string to the file.

    '''
    


def reset():
    clear_data()    # clear out data structure
    Taxpayer.reset_data()       # clear out data model
    print('All data reset..')

def clear_data():
    global taxpayerlist
    taxpayerlist.clear()

def search():
    global taxpayerlist
    '''
    1.Prompt user to enter name
    2.Initialize a bool variable to track found or not
    3.For each taxpayer in the list:
       3.1 if the name matches
             flip the bool
             print the taxpayer
             (if name is not duplicated, stop the loop here)
    4.Check the bool afterwards to report if name was not found.

    '''
    name_in = input('Type name >> ')
    found = False
    for taxpayer in taxpayerlist:
        if taxpayer.matches_name(name_in):
            found = True
            print(taxpayer)
    if not found:
        print(f'{name_in:s} not found in taxpayers')


#main
functions = {
    1:submit,
    2:load,
    3:summary,
    4:save,
    5:display,
    6:search,
    7:reset, 
}

while True:
    print('1.Submit 2.Load 3.Summary 4.Save 5.Display 6.Search 7. Reset 8. Exit')
    choice = int(input('Enter choice:  '))
    if choice == 8:
        clear_data()
        break
    if choice not in functions:
        print('Invalid Choice!')
        continue
    functions[choice]()

print('Goodbye!')

# CODE TO Deal with FILE LOCATION ISSUES
# ENSURE input file is in same folder as .py file.
""" To Make your code work with text files in same folder as the .py files regardless of environment and editor used:
use this code. (the import statement goes as the first line in your .py file, the rest goes where you do the file open and read, and replace the .txt with your filename
this assumes your input file is in same folder as .py file

import os.path   #first line up top in .py

filepath = os.path.dirname(__file__)
filename = os.path.join(filepath, 'test.txt')  # replace test.txt with what you need

with open(filename, 'r') etc..
"""
