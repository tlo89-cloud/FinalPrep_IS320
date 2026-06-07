""" Trevor Lorenz A2 Question 1 04/21/2026.

User inputs weight in pounds, my program finds the shipping rate,
then uses the rate found to compute the shipping cost, based on weight
^these should both be functions

main reads user input, calls each function, then prints shipping cost
"""


# funcitons

# func 1: calculate shipping rate
def calc_ship_rate(weight):   # we would add in ship_type as a paramater
    # if ship_type == 1:
        #  if weight >= 10.0:
        #     ship_rate = 0.20
        # else:
        #     ship_rate = 0.15
    # else:
        # same as above but with accounting for standard type

    # return ship_rate

    if weight >= 10.0:
        ship_rate = 0.20
    else:
        ship_rate = 0.15
    return ship_rate


# func 2: calculate shipping cost
def calc_ship_cost(weight, ship_rate):
    ship_cost = weight * ship_rate
    return ship_cost


# main
weight = float(input("Please input weight of order\n>>>"))
# shipping_type = int(input("Input express or standard shipping (1, 0)\n>>>"))
ship_rate = calc_ship_rate(weight)
ship_cost = calc_ship_cost(weight, ship_rate)

# output
print(f"Shipping cost: ${ship_cost:.2f}")

"""
We will create an input request from the user to specify
express or standard (1 or 0), then we will create an if statement
outside of the above if statement within the calc_shipping_rate
that handles the express v standard cases seperatley, and we will
add in ship_type as an additional parameter in the function header.

^^ commented out functions above for reference
"""
