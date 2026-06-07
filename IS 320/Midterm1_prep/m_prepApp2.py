'''
Problem 2

SUBMIT
user inputs: score, graded or not
displayed output: grade
letter grade:    graded:  A above 80 B otherwise
not graded:  P at or above 40   F otherwise
function:  compute grade

SUMMARY
display average score for graded, average score for pass/fail, 
display count of 100s  among graded inputs and 0s among pass/fail inputs
functions: one for each average

RESET
gets ready for new series of inputs

EXTRAS
Validate score as being in 0..100 range
'''
# globals
total_g_score = 0.0
count_g = 0
total_pf_score = 0.0
count_pf = 0
count_100 = 0
count_0 = 0

# functions

def submit():
    global total_g_score, count_g, total_pf_score, count_pf, count_100, count_0
    score = int(input("Input score >>> "))
    while score < 0 or score > 100.0:
        print(f"You input {score}, please enter a score from 0...100")
        score = int(input("Input score within 0...100 >>> "))
    graded = int(input("Input graded(1) or not (0) >>> "))

    if graded:
        total_g_score += score
        count_g += 1
        if score > 80:
            grade = "A"
            if score == 100:
                count_100 += 1
                
        else:
            grade = "B"
    else:
        total_pf_score += score
        count_pf += 1
        if score >= 40:
            grade = "P"
        else:
            grade = "F"
            if score == 0:
                count_0 += 1
    print(grade)


def average_g_score():
    global total_g_score, count_g, total_pf_score, count_pf, count_100, count_0
    if count_g <= 0:
        return None
    else:
        avg = total_g_score / count_g
        return avg


def average_pf_score():
    global total_g_score, count_g, total_pf_score, count_pf, count_100, count_0
    if count_pf <= 0:
       return None
    else:
        avg = total_pf_score / count_pf
        return avg


def summary():
    global total_g_score, count_g, total_pf_score, count_pf, count_100, count_0
    average_g = average_g_score()
    average_pf = average_pf_score()
    print(f"Average graded score: {average_g:.2f}")
    print(f"Average P/F score: {average_pf:.2f}")    
    print(f"Count of 100s: {count_100:d}")
    print(f"Count of 0s: {count_0:d}")


def reset():
    global total_g_score, count_g, total_pf_score, count_pf, count_100, count_0
    total_g_score = 0.0
    count_g = 0
    total_pf_score = 0.0
    count_pf = 0
    count_100 = 0
    count_0 = 0
    print("Ready for new data!")


quit = False
while not quit:
   print('1.Submit 2.Summary 3.Reset. 4.Exit')
   print('Choose 1,2,3, or 4')
   choice = int(input('>>'))
   if choice == 1:
       submit()
   elif choice == 2:
       summary()
   elif choice == 3:
       reset()
   elif choice == 4:
       quit = True
   else:
       print('Invalid choice! Choose 1,2,3, or 4')
print('Bye!')


