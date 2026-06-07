'''
Object Oriented Programming

submit/load inputs name, income
tax rate 10% below 100000 else 15%


guidelines:
every method(function) in class has 'self' as the first parameter.
two special functions required:
__init__(self, <user inputs>)    to make a taxpayer  <-- data coming into the class
__str__(self)     to make an str(taxpayer) -> data going out of class

syntax examples:
student = Student(name, score)    make a student object, of Student class

student.display_line()   call the display_line() function for the student

'''

# documentation inside class : move this inside class
"""
attributes: name:str, income:float, tax:float
methods: __init__()  __str__()
    compute_tax()  display_line()  csv_line()
"""


# globals
taxpayerlist = []  # a list to store taxpayer objects


# classes
class Taxpayer:
    def __init__(self, name, income):      # self represents the object itself (e.g. taxpayer)
        self.name = name    # create an attribute 'name' for self
        self.income = income
    
        # update totals

    def __str__(self):      # every function in classes must have first paramater be self
        '''must return string. supports the print. '''
        return f'''
        Name\t:{self.name:s}
        Income\t:{self.income:.2f}
        '''

    # make a custom output function for use by display
    def display_line(self):
        return f'|{self.name:<10s}|{self.income:>10.2f}|'

    def csv_line(self):
        return f'|{self.name:s}|{self.income:.2f}|'



# end class Taxpayer


# functions
def submit():
    pass   # <-------remove
    # read inputs as a line
    line_in = input('Enter name and income')
    # process the line
    # 0 extract and validate inputs
    list_in = line_in.split()

    name = list_in[0]
    income = float(list_in[1])
    # 1 make a taxpayer object
    taxpayer = Taxpayer(name, income)
    # 2 add it to the global list
    taxpayerlist.append(taxpayer)

    # print the object
    print(1000.0)       # call the str() method of float class
    print(taxpayer)     # call the str() method of Taxpayer class
    # print(type(10.5))
    # print(type('hi'))
    # print(type(Taxpayer()))


def load():
    pass


def display():
    global taxpayerlist

    for taxpayer in taxpayerlist:
        print(taxpayer.display_line())
        # print(taxpayer)     # uses the str()
        # print(taxpayer.__str__()) ^ is what is happening here

def summary():
    pass


def save():
    global taxpayerlist
    out_data = ''
    for taxpayer in taxpayerlist:
        line = taxpayer.csv_line()
        out_data += line+'\n'

    with open('oop1out.txt, w') as outfile:
        outfile.write(out_data.rstrip('\n'))



def reset():
    clear_data()


def clear_data():
    global taxpayerlist
    taxpayerlist.clear()


def search():
    pass


# main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Save 5.Display 6.Search 7. Reset 8. Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       load()
   elif choice == 3:
       summary()
   elif choice == 4:
       save()

   elif choice == 5:
       display()
   elif choice == 6:
       search()
   elif choice == 7: 
       reset()    
       print('Data cleared. Ready for new series...')
   elif choice == 8:
       quit = True   
       clear_data()
   else:
       print('Invalid Choice!')


#NOTES

#Terminology
'''
Object - a variable
income, tax, name > variables
OOP treats tax_payer is a variable

taxpayer.compute tax()

variables + functions -> object



a data structure like a dictionary - contains multiple variables/values
an object -  adds functions to it.   variables plus functions.
student object can contain  - name, score, grade, compute_grade()

Class is the blueprint to make Objects.
Class ->  Type
Object -> Variable

a student object - from Student class
an order object - from Order class.

we define a Class.  then make objects as copies of it.
an Object is an instance of the Class.

a Class contains multiple functions, and variables.
The functions are called Methods.

A special method, used to make a new object -   __init__()
A special method, used to support printing -   __str__()

Once an object is created, we can treat it like any other variable.
We can make a list of student objects,
we can print student objects.

self - when inside the class, we use self to refer to the object 
self.score   - score attribute of this object
self.compute_grade()  - compute_grade() method of this object

when outside the class, we use the object's name
student.score
student.compute_grade()


print and str and __str__()
str(student) generates a string version of student.
what it really does is to call the method __str__()

print(student) will, behind the scenes, do print(str(student)),
which in turn, is doing print(student.__str__())

So if we have an __str__() method that generates a string for
the student, the print will use that.

Or, briefly, just use the return statement in def __str__() to
control what print(student) does.


'''




#CODE TO Deal with FILE LOCATION ISSUES
#ENSURE input file is in same folder as .py file.
""" To Make your code work with text files in same folder as the .py files regardless of environment and editor used:
use this code. (the import statement goes as the first line in your .py file, the rest goes where you do the file open and read, and replace the .txt with your filename
this assumes your input file is in same folder as .py file

import os.path   #first line up top in .py

filepath = os.path.dirname(__file__)
filename = os.path.join(filepath, 'test.txt')  # replace test.txt with what you need

with open(filename, 'r') etc..
"""