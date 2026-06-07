""" Trevor Lorenz HW 4 Problem 1 05/01/2026.

Collects 2 inputs from user, score and grading basis
On grade basis: score > 80 = A, otherwise B
On P/F basis: score >= 40 = Pass, otherwise Fail

Program computes the grade using a function and outputs a
single result, for each submission

The summary function displays: total number of inputs, number of
A, B, P, & F grades, avg score for grade basis inputs, and avg
score for pass/fail inputs

Input: score(int), grading_status(int)
Output: grade(str)
"""

# globals
num_a = 0  # count all a grades
num_b = 0  # count all b grades
num_p = 0  # count all passes
num_f = 0  # count all fail
total_score_grade_basis = 0.0  # sum total grade basis score
total_score_p_f = 0.0  # sum total p/f score

# functions

def calculate_grade(grd_status, scr):
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    if grd_status:
        total_score_grade_basis += scr
        if scr > 80.0:
            grade = "A"
            num_a += 1
        else:
            grade = "B"
            num_b += 1
    else:
        total_score_p_f += scr
        if scr >= 40.0:
            grade = "P"
            num_p += 1
        else:
            grade = "F"
            num_f += 1
    return grade


def calculate_avg_grd_basis_score():
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    
    num_letter_inputs = num_a + num_b
    if num_letter_inputs > 0:
        avg_gd_basis = total_score_grade_basis / num_letter_inputs
    else:
        avg_gd_basis = None
    return avg_gd_basis


def calculate_avg_p_f_basis_score():
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    num_pf_inputs = num_p + num_f
    if num_pf_inputs > 0:
        avg_p_f = total_score_p_f / num_pf_inputs
    else:
        avg_p_f = None
    return avg_p_f


def submit():
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    score = int(input("Input Score>>"))
    grading_status = int(input("Input grade basis (1 = grade_basis, 0 = Pass/Fail)>>"))
    grade = calculate_grade(grading_status, score)
    print(grade)


def summary():
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    avg_gd_basis = calculate_avg_grd_basis_score()
    avg_p_f = calculate_avg_p_f_basis_score()
    total_score = num_a + num_b + num_p + num_f
    print(f"Total Grade Count: {total_score:d}")
    print(f"Number of A's: {num_a:d}")
    print(f"Number of B's: {num_b:d}")
    print(f"Number of P's: {num_p:d}")
    print(f"Number of F's: {num_f:d}")
    if avg_gd_basis is not None:
        print(f"Grade Basis Avg Score: {avg_gd_basis:.2f}")
    else:
        print("No Data")
    if avg_p_f is not None:
        print(f"Pass/Fail Avg Score: {avg_p_f:.2f}")    
    else:
        print("No Data")


def reset():
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    num_a = 0
    num_b = 0
    num_p = 0
    num_f = 0
    total_score_grade_basis = 0.0
    total_score_p_f = 0.0 


quit = False
while not quit:
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    choice = int(input('Enter choice: '))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
        print("Ready for new series..")
    elif choice == 4:
        quit = True
    else:
        print('Invalid Choice!')