


# globals
count_g = 0
g_score_total = 0.0
count_pf = 0
pf_score_total = 0.0
count_100 = 0
count_0 = 0


def compute_results(score, graded):
    global count_g, g_score_total, count_pf, pf_score_total, count_100, count_0
    if graded:
        count_g += 1
        g_score_total += score
        if score > 80:
            grade = 'A'
        else:
            grade = 'B'
    else:
        count_pf += 1
        pf_score_total += score
        if score >= 40:
            grade = 'P'
        else:
            grade = 'F'
    if score == 100:
        count_100 += 1
    if score == 0:
        count_0 += 1
    return grade


def submit():
    global count_g, g_score_total, count_pf, pf_score_total, count_100, count_0
    score = float(input("Input score >>> "))
    while score < 0 or score > 100:
        print("CRuh enter a number in rage 1...100")
        score = float(input("Input score (1...100)>>> "))

    graded = int(input("Input graded (1) or not (0) >>> "))
    grade = compute_results(score, graded)
    print(f"Your grade is: {grade:s}")


def calc_avg_graded_score():
    global count_g, g_score_total, count_pf, pf_score_total, count_100, count_0
    if count_g > 0:
        avg = g_score_total / count_g
    else:
        avg = None
    return avg


def calc_avg_pf_scores():
    global count_g, g_score_total, count_pf, pf_score_total, count_100, count_0
    if count_pf > 0:
        avg = pf_score_total / count_pf
    else:
        avg = None
    return avg


def summary():
    global count_g, g_score_total, count_pf, pf_score_total, count_100, count_0
    avg_graded_scores = calc_avg_graded_score()
    avg_pf_scores = calc_avg_pf_scores()
    if avg_graded_scores is None:
        print("Mayne fuc all at data you aint send shi")
    else:
        print(f"yo avg grd score is {avg_graded_scores:.2f}")
    
    if avg_graded_scores is None:
        print("Mayne fuc all at data you aint send shi")
    else:
        print(f"yo avg pf score is {avg_pf_scores:.2f}")


def reset():
    global count_g, g_score_total, count_pf, pf_score_total, count_100, count_0
    count_g = 0
    g_score_total = 0.0
    count_pf = 0
    pf_score_total = 0.0
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
