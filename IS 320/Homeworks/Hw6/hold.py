""" Trevor Lorenz HW 6 05/23/2026.

"""
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
taxpayers = {}
# ^ taxpayer dcitionary includes key: taxpayerID, and values name, status,
# income, and tax

# taxpayerlist = []  # a list to store taxpayer objects

#  ____________________________
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
#  ____________________________


# end class Taxpayer


# functions
def submit():
    # read inputs as a line
    line_in = input('Enter name, married or not (1,0), and income (3 values) > ')
    # 0 extract and validate inputs
    list_in = line_in.split()
    name = list_in[0]
    married = int(list_in[1])
    income = float(list_in[2])

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

