""" Trevor Lorenz Hw1 Question 1 04/06/2026.

User inputs protein, carb, and fat weights, and
program outputs their respective weights, and total
calories.

input: protein weight: float
input: carb weight: float
input: fat weight: float

output: protein weight: float
output: carb weight: float
output: fat weight: float
output: total calories: float

"""

# Inputs
protein_weight = float(input("Enter protein weight:\n>>>"))
carb_weight = float(input("Enter carb weight:\n>>>"))
fat_weight = float(input("Enter fat weight:\n>>>"))

# Initialization
cal_per_fat = 9.0
cal_per_protein = 4.0
cal_per_carb = 4.0

# Computations
cal_fat = cal_per_fat * fat_weight
cal_protein = cal_per_protein * protein_weight
cal_carb = cal_per_carb * carb_weight

total_cals = cal_protein + cal_carb + cal_fat

# Outputs
print(f"Protein: {protein_weight:.2f}g")
print(f"Carbs: {carb_weight:.2f}g")
print(f"Fat: {fat_weight:.2f}g")
print(f"Total: {total_cals:.2f}")
