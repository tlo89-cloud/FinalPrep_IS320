'''
input is score, integer. grade is a for score above 80, b otherwise
use a computer_grade function.

input: score: int
out: Letter grade: str

'''


# functions
def calculate_score(score):
    if score > 80:
        letter_grade = "A"
    else:
        letter_grade = "B"

    return letter_grade


# main
score = int(input("Enter Score\n>>>"))

# output

print(score, calculate_score(score))
