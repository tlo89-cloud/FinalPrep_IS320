"""
Collect two inputs from the user, score as integer, and whether on
grade basis or not. Not on grade basis means on Pass/Fail basis.

Compute grade using a function. On grade basis: score above 80 is
A else B. Pass/Fail basis: score at or above 40 is pass, else fail.

Package input, computations and output into a submit function, and
call that a few times from main. Submit displays the grade. Create

a summary function that displays the number of inputs, number of As,
Bs, Pass, and Fail. Display the average score for inputs on grade basis
and pass/fail basis respectively as well. Use two separate average
functions. You call each from summary. Review your global variables
to see if you can reduce their number. Hint: if a global variable can
be easily derived from other global variables, you can calculate it
on demand, getting rid of the global variable.

Submit shows a single output: the grade (A B P or F)
Summary shows five counts and two averages.

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
    score = float(input("Input Score>>"))
    grading_status = int(input("Input grade basis (1 = grade_basis, 0 = Pass/Fail)>>"))
    grade = calculate_grade(grading_status, score)
    print(grade)


def summary():
    global num_a, num_b, num_p, num_f, total_score_grade_basis, total_score_p_f
    avg_gd_basis = calculate_avg_grd_basis_score()
    avg_p_f = calculate_avg_p_f_basis_score()
    total_score = num_a + num_b + num_p + num_f
    print(f"Number of A's: {num_a:d}")
    print(f"Number of B's: {num_b:d}")
    print(f"Number of P's: {num_p:d}")
    print(f"Number of F's: {num_f:d}")
    print(f"Total Grade Count: {total_score:d}")
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