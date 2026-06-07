"""A3.py  04.28.26 Developed By Trevor Lorenz.

In this app, the submit works correctly. Run the app and verify.
We require:
summary outputs: average score, and the number of A grades and
the number of B grades. SAMPLE OUTPUTS AT END OF THIS FILE.

You can update your globals in submit, or in the compute_grade function.

compute_average_score() function provides the average score for
summary function.
reset: gets ready for a new series of outputs.
code the above three functions, making updates as needed to the
code you already have.
your code *MUST* follow patterns shown in lecture 8.

submit output: grade: str
summary outputs: average_score:float, count_A:int  count_B:int
"""
# globals
total_scores = 0.0
scores_count = 0
a_count = 0
b_count = 0


# functions
def compute_grade(sc):
    global total_scores, scores_count, a_count, b_count
    if sc > 80:
        grd = 'A'
        a_count += 1
    else:
        grd = 'B'
        b_count += 1
    total_scores += sc
    scores_count += 1
    return grd


def submit():
    global total_scores, scores_count, a_count, b_count
    score = int(input('Enter score >'))

    letter_grade = compute_grade(score)

    print(f'Your grade is: {letter_grade:s}')
# end submit


def compute_average_score():
    global total_scores, scores_count, a_count, b_count
    if scores_count == 0:
        return "No data"
    else:
        avg = total_scores / scores_count
        return avg


def summary():
    # summary outputs: average_score:float, count_A:int  count_B:int
    global total_scores, scores_count, a_count, b_count
    if scores_count <= 0:
        print("No data")
    else:
        avg = compute_average_score()
        print(f"Average score: {avg:.2f}")
        print(f"Number of A grades: {a_count:d}")
        print(f"Number of B grades: {b_count:d}")

# end summary


def reset():
    global total_scores, scores_count, a_count, b_count
    total_scores = 0.0
    scores_count = 0
    a_count = 0
    b_count = 0
# end reset


# main  #don't edit the lines below
quit = False
while not quit:
    print('1.Submit 2.Summary 3.Reset 4.Exit')
    choice = int(input('Enter choice:  '))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
    elif choice == 4:
        quit = True
    else:
        print('Invalid Choice!')
print('Goodbye!')


'''
SAMPLE OUTPUTS
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  1
Enter score >90
Your grade is: A
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  1
Enter score >9
Your grade is: B
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  1
Enter score >80
Your grade is: B
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  2
Average Score: 59.67
Number of A grades: 1
Number of B grades: 2
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  3
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  2
No data
Number of A grades: 0   It is okay if these do not show here
Number of B grades: 0  It is okay if these do not show here
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  1
Enter score >70
Your grade is: B
1.Submit 2.Summary 3.Reset 4.Exit
Enter choice:  2
Average Score: 70.00
Number of A grades: 0
Number of B grades: 1
'''
