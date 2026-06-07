""" Trevor Lorenz HW 6 05/23/2026.

Manages a taxpayer dictionary with submit, load, and save functionality.
Computes tax based on marital status and income.

input: name (str), married (int), income (float)
output: tax (float), taxpayer details displayed and saved to file
"""

# globals
taxpayers = {}
taxpayer_id = 10000
new_to_save = 0

# functions


def process_line(ln_in, sep=None):
    """Process one taxpayer input line and add entry to taxpayers dictionary."""
    global taxpayers, taxpayer_id, new_to_save

    list_in = ln_in.split(sep)
    name = list_in[0]
    married_str = list_in[1]
    income_str = list_in[2]

    while True:
        try:
            married = int(married_str)
            assert married == 1 or married == 0
            break

        except ValueError:
            print('Status must be an integer.')
            married_str = input('Enter married or not (1,0) > ')

        except AssertionError:
            print('Status must be 1 or 0.')
            married_str = input('Enter married or not (1,0) > ')

    while True:
        try:
            income = float(income_str)
            assert income > 0 and income <= 500000
            break

        except ValueError:
            print('Income must be a number')
            income_str = input('Input income > ')

        except AssertionError:
            print('Income must be positive and less than or equal to 500,000')
            income_str = input('Input income > ')

    tax = compute_tax(married, income)
    taxpayer_details = {'Name': name, 'Income': income, 'Status': married, 'Tax': tax}
    taxpayer_id += 1
    new_to_save = 1
    taxpayers[taxpayer_id] = taxpayer_details


def print_taxpayer(tid):
    """Formats and prints the taxpayer details based on a taxpayer ID"""
    global taxpayers, taxpayer_id, new_to_save
    taxpayer_details = taxpayers[tid]
    print(f'''
          TaxpayerID:\t{tid:d}
          Name:\t\t{taxpayer_details['Name']:s}
          Status:\t\t{taxpayer_details['Status']:d}
          Income:\t\t{taxpayer_details['Income']:.2f}
          Tax:\t\t{taxpayer_details['Tax']:.2f}
          ''')


def submit():
    """Read taxpayer inputs from user and add taxpayer to dictionary."""
    global taxpayers, taxpayer_id, new_to_save
    line_in = input('Enter name, married or not (1,0), and income > ')
    while len(line_in.split()) != 3:
        print('Must be three arguments')
        line_in = input('Enter name, married or not (1,0), and income > ')

    process_line(line_in)
    print_taxpayer(taxpayer_id)


def compute_tax(married, income):
    """Compute and return tax based on marital status and income."""
    global taxpayers, taxpayer_id, new_to_save
    if married:
        if income > 100000:
            tax_rate = 0.20
        else:
            tax_rate = 0.10
    else:
        if income > 70000:
            tax_rate = 0.15
        else:
            tax_rate = 0.08

    tax = income * tax_rate

    return tax


def load():
    """Load taxpayer records from a text file into the dictionary."""
    global taxpayers, taxpayer_id, new_to_save
    filename = input('File name for load >> ')
    count = 0

    with open(filename, 'r') as loadfile:
        for line in loadfile:
            process_line(line, ',')
            count += 1
    print(f'{count:d} taxpayers loaded from {filename:s}')


def save():
    """Save taxpayer records from the dictionary to a text file."""
    global taxpayers, taxpayer_id, new_to_save
    if not taxpayers:
        print('No taxpayer data to save.')
        return

    if new_to_save:
        count = 0
        out_string = ''
        for tid in taxpayers:
            taxpayer_details = taxpayers[tid]
            name = taxpayer_details['Name']
            income = taxpayer_details['Income']
            married = taxpayer_details['Status']
            tax = taxpayer_details['Tax']
            line = f'{tid:d},{name:s},{income:.2f},{married:d},{tax:.2f}'
            out_string += line + '\n'
            count += 1
        filename = 'dicthw6.txt'
        with open(filename, 'w') as savefile:
            savefile.write(out_string.rstrip('\n'))
        new_to_save = 0

        print(f'{count:d} taxpayers saved to {filename:s}')

    else:
        print("Saved data already caught up: no need to save more data")


functions = {
            1: submit,
            2: load,
            3: save
             }

# main
while True:
    print('1.Submit 2.Load 3.Save 4.Exit')
    choice = int(input('Enter 1,2,3, or 4 >> '))

    if choice == 4:
        print("Goodbye!")
        break
    if choice not in functions:
        print('Invalid Choice')
        continue

    functions[choice]()
