'''
Python Lab 1
Name: Trevor Lorenz
Class: IS 320
Description: Lab Problem 3
'''

# Problem 3

'''
Collect 6 inputs from user, all info 
about students. 
Input 1: student name
Input 2-4: hw scores
Input 5-6: test scores out of 30, float
Scaled Total Score is calc out of 100, 
homework is scaled to 60 pts, test is scaled to 
40 points
'''

# Inputs

name = input('Enter your name \n >>')
hw_1 = int(input('Enter your hw_1 score \n >>'))
hw_2 = int(input('Enter your hw_2 score \n >>'))
hw_3 = int(input('Enter your hw_3 score \n >>'))
test_1 = int(input('Enter your test_1 score \n >>'))
test_2 = int(input('Enter your test_2 score \n >>'))

hw_weight = 0.6
test_weight = 0.4

# Computation
weighted_hw = hw_weight * ((hw_1 + hw_2 + hw_3)/150)
weighted_test = test_weight * ((test_1 + test_2)/60)
total_score = (weighted_hw + weighted_test) * 100

# Output
print("Name:", name)
print(f"Homework 1: {hw_1:d}/50")
print(f"Homework 2: {hw_2:d}/50")
print(f"Homework 3: {hw_3:d}/50")
print(f"Test 1: {test_1:d}/30")
print(f"Test 2: {test_2:d}/30")
print()
print(f"Scaled Total Score: {total_score:d}/100")
