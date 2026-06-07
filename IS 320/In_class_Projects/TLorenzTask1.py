""" Trevor Lorenz Functions Self Study 04.17.2026


"""


# Problem 1
def sum_series(first, last, number_of_elements):
    sum = (first + last) / 2 * number_of_elements  #count of numbers in the series
    return sum

# for example: The series 5,6,7 has first = 5, last = 7, number_of_elements = 3
# and the sum is then: 12 / 2 * 3 = 18

# I want to find the sum of numbers 1,2,....98,99,100.  
# The function above has the correct computation for it.
# Make the code below work, so that I get 5050 as result displayed


my_sum = sum_series(1, 100, 100)
print(my_sum)


# Problem 2
def compute_square(num):
    my_square = num ** 2
    return my_square


my_square = compute_square(101)
print(my_square)


# Problem 3
def compute_product(num1, num2):
    my_product = num1 * num2
    return my_product


my_product = compute_product(7, 3)
print(my_product)


# Problem 4
# tax rate is 10% for income below 100,000, and
# 15% otherwise.
# define your function here to make the call below work.


def compute_tax_rate(income):
    if income < 100000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    return tax_rate


income = float(input('Enter income >>'))
tax_rate = compute_tax_rate(income)
tax = income * tax_rate
print(tax)

# Problem 5
# letter grade is A for score above 70, B otherwise.
# assume score will always be
# in the range 0..100
# define your function here.


def calculate_grade(score):
    if score > 70:
        letter_grade = 'A'
    else:
        letter_grade = 'B'
    return letter_grade


score = int(input('Enter your score >>'))
# add your function call here so that the print below works.
grade = calculate_grade(score)
print(grade)


# Problem 6
# user enters: prot_gms, carb_gms, fat_gms display: total calories.
# protein - 4 cal per gm
# carbs - 4 cal per gm
# fat - 9 cal per gm

# write a function to compute calories. Takes three weights as inputs, output
# is the total calories. Write code to read the three inputs, call the
# function, and to display the total calories.


def calculate_calories(prot_gms, carb_gms, fat_gms):
    protien_cal_per_gm = 4
    carb_cal_per_gm = 4
    fat_cal_per_gm = 9

    cal_from_protien = protien_cal_per_gm * prot_gms
    cal_from_carb = carb_cal_per_gm * carb_gms
    cal_from_fat = fat_cal_per_gm * fat_gms

    total_calories = cal_from_protien + cal_from_carb + cal_from_fat

    return total_calories


prot_gms = float(input('Enter protien grams >>'))
carb_gms = float(input('Enter carb grams >>'))
fat_gms = float(input('Enter fat grams >>'))

print(calculate_calories(prot_gms, carb_gms, fat_gms))
