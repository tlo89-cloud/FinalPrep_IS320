""" Trevor Lorenz Lab2 Drill 04/09/2026.

User inputs protein, carb, and fat weights, and
program outputs their respective weights, and total
calories.
"""

# Problem 1
# User enters an integer. Your app displays
# Positive, Negative, or Zero based on its value.
'''
entry = int(input("Please input number here:\n>>>"))

if entry > 0:
    print("Positive")
elif entry < 0:
    print("Negative")
else:
    print("Zero")
'''
# Problem 2
# Just not doing allat.

# Problem 3
# Set three variables a,b,c in your program to three integers. 
# For example, a = 10 b = 12 c = 15 Find the highest and lowest number. 
# Restriction: use only: if statements with simple conditions like a > b 
# that compare two numbers. (no and/or, no advanced techniques or built-in 
# functions, no python-specific techniques like a < b < c)
'''
a = 3
b = 3
c = 15


highest = a
if b > highest:
    highest = b
if c > highest:
    highest = c

lowest = a
if b < lowest:
    lowest = b
if c < lowest:
    lowest = c

print(f'Highest: {highest}')
print(f'Lowest: {lowest}')
'''


# Problem 7
# Debug
'''
score = 72
grade = 0
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)
'''
