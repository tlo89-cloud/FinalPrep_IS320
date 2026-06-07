# Trevor Lorenz, SS2 05.13.2026
# TASK  1:

# Store unit prices in a dictionary with keys
# Artichokes, Carrots, Beets
# Fill in the { } below
unit_prices = {'Artichokes': 1.5, 'Beets': 2.5, 'Carrots': 1.0}

wt_a = float(input('Weight for artichokes >>'))
wt_b = float(input('Weight for beets >>'))
wt_c = float(input('Weight for carrots>>'))

# Now try to rewrite the line 9 in the cell above, using the
# unit_prices dictionary

price = (wt_a * unit_prices['Artichokes']
         + wt_b * unit_prices['Beets']
         + wt_c * unit_prices['Carrots'])

print(price)

# TASK 2

# place prices in dictionary as before (or re-use the dict from
# previous cell)
weights = {}  # initialize an empty dictionary

# fill weights dictionary with inputs
# for example,
weights['Artichokes'] = float(input('Weight for artichokes >>'))
weights['Beets'] = float(input('Weight for beets >>'))
weights['Carrots'] = float(input('Weight for carrots >>'))

# use both dictionaries, the one for unit prices from previous cell, and the
# weights dictionary, to compute the price below.

price = 0
for key in weights.keys():
    price += weights[key] * unit_prices[key]
print(price)

# print(price)
# Review the code, and consider: can we use the for loop? We are
# collecting the weight for each key in the unit_prices dictionary.
# Hint: you can use the f'....{..:..}' format inside an input statement.
# If you can figure out how to use a for loop, implement it.
# If not, leave it be.


# TASK 3 redo the code below in a new cell, attempting to implement the four
# items listed in the text cell below. This is slightly more challenging than
# prior tasks.


def submit():
    unit_prices = {'Artichokes': 1.5, 'Beets': 2.5, 'Carrots': 1.0}
    order = {}
    choice_dict = {1: 'Artichokes', 2: 'Beets', 3: 'Carrots'}

    choice = int(input('1.Artichokes 2 Beets 3 Carrots. Enter 1 2 or 3>>'))
    order['product'] = choice_dict[choice]
    order['weight'] = float(input('Enter weight ordered in lb >>'))
    order['price'] = unit_prices[order['product']] * order['weight']

    print(order['price'])


quit = False
while not quit:
    print('1.Submit, 2.Quit')
    print('Choose 1 or 2')
    choice = int(input('>>'))
    if choice == 1:
        submit()
    elif choice == 2:
        quit = True
    else:
        print('Invalid choice! Choose 1 or 2')
print('Bye!')
