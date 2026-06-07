'''
Python Lab 1
Name: Trevor Lorenz
Class: IS 320
Description: Lab Problem 1
'''

# Problem 1
'''
Takes in protein, carb, and fat weights, and outputs
their respective weights, and total carb content

Note: current values are placeholders
'''

protien_weight = 2
carb_weight = 2
fat_weight = 3

cal_fat = 9 * fat_weight
cal_protien = 4 * protien_weight
cal_carb = 4 * carb_weight

total_carbs = cal_protien + cal_carb + cal_fat
print(protien_weight, carb_weight,
      fat_weight, total_carbs)
