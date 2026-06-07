'''Lecture 3 App4 04.07.26 Developed by Trevor

App 4:
A score is on grade basis or not.
User enters 1 for grade basis, 0 for not graded.
User enters score (0..100) integer.
grade basis:  >= 80  A  else B
not grade basis  > 40 P(ass)  else F(ail)
'''

score = int(input("Input score(0..100)\n>>>"))
status = int(input("Input graded status (1 = graded, 0 = not graded)\n>>>"))

if status == 1:
    if score >= 80:
        grade = "A"
    else:
        grade = "B"
else:
    if score >= 40:
        grade = "P"
    else:
        grade = "F"

print(f"Letter grade is; {grade:s}")


