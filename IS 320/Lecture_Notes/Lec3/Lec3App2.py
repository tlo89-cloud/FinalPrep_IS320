'''Lecture 3 App2 04.07.26 Developed by Trevor

User enters score (integer in range 0..100)
letter grade A,B or C is computed and displayed.
80-100 A
60-79 B
0-59 C
input: score: int
output: letter_grade : str
'''


# inputs
score = int(input("Enter score (0..100) >"))

# computations
if score >= 80:
    letter_grade = "A"
elif score >= 60:
    letter_grade = "B"
else:
    letter_grade = "C"

# output
print(f'Score: {score:d}')
print(f'Grade: {letter_grade:s}')
