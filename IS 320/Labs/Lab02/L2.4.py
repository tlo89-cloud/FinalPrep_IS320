""" Trevor Lorenz Lab2 Problem 4 04/09/2026.

Collects 5 inputs from user about a student: student name,
2 homework scores out of 50, 2 test scores out of 30 (floats)

Scaled total score is calc. out of 100, hw is worth 60 pts, tests
are worth 40 pts.

Grade calculated out of 100, 90+ = A, 80-90 = B, 60+ = C, rest get D

If a student would get a B, but one test score = 30, the grade changes
to an A

"""

# inputs
name = str(input("Please input student name:\n>>>"))
hw_1 = float(input("Please input homework 1 score: /50\n>>>"))
hw_2 = float(input("Please input homework 2 score: /50\n>>>"))
test_1 = float(input("Please input test 1 score: /30\n>>>"))
test_2 = float(input("Please input test 2 score: /30\n>>>"))

# initilization
homework_weight = 60.0
test_weight = 40.0

# computations
total_hw_score = (hw_1 + hw_2)/100
total_test_score = (test_1 + test_2)/60
weighted_hw_score = total_hw_score * homework_weight
weighted_test_score = total_test_score * test_weight


scaled_total_score = weighted_hw_score + weighted_test_score

if scaled_total_score > 90.0:
    grade = 'A'
elif scaled_total_score >= 80.0:
    grade = 'B'
elif scaled_total_score >= 60.0:
    grade = 'C'
else:
    grade = 'D'

if grade == 'B':
    if test_1 == 30.0:
        grade = 'A'
    if test_2 == 30.0:
        grade = 'A'

# output
print(f"Name:\t{name}")
print()
print(f"Homework 1:\t{hw_1:.1f}/50")
print(f"Homework 2:\t{hw_2:.1f}/50")
print()
print(f"Test 1:\t{test_1:.1f}/30")
print(f"Test 2:\t{test_2:.1f}/30")
print()
print(f"Scaled Total Score:\t{scaled_total_score:.2f}/100")
print(f"Grade:\t{grade}")
