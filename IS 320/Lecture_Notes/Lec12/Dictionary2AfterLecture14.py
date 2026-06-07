""" Trevor Lorenz

"""

# students = {
#     1001: {'Name': 'Alex', 'Score': 100, 'Grade': 'A'},
#     1002: {'Name': 'Alex', 'Score': 77, 'Grade': 'B'},
#     1003: {'Name': 'Denise', 'Score': 90, 'Grade': 'A'},
#     1004: {'Name': 'Emily', 'Score': 40, 'Grade': 'B'}
#     }

# New code and shi
students = {}
student_id = 1000


def compute_grade(sc):
    if sc > 80:
        grade = 'A'
    else:
        grade = 'B'
    return grade


def process_line(ln_in):
    # collects a line like Adam 100 and generates a student entry in global dict. 
    global student_id
    list_in = ln_in.split()
    name = list_in[0]
    score = int(list_in[1])

    grade = compute_grade(score)
    student_details = {'Name': name, 'Score': score, 'Grade': grade}
    student_id += 1
    students[student_id] = student_details


def submit():
    line_in = input('enter name and score')
    process_line(line_in)

    print(student_id, students[student_id])


def load():
    filename = input('File name for load >> ')
    with open(filename, 'r') as loadfile:
        for line in loadfile:
            process_line(line, ',')

# functiions

def display():
    """Show the contents of the dictionary."""

    # empty check
    if not students:
        print('No student data to display.')
        return 
    width = 46  # 12 + 15 + 7 + 7 + (4+1)
    line = '-' * width
    print(line)
    print(f'|{"Student ID":^12s}|{"Name":^15s}|{"Score":^7s}|{"Grade":^7s}|')
    print(line)
    for sid in students:
        student_details = students[sid]
        # print(student_details)
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        print(f'|{sid:<12d}|{name:<15s}|{score:^7d}|{grade:^7s}|')
    # end for
    print(line)
# left justify <
# right > center ^
# floats to be right justified.   >10.2f


def save():
    """Save the contents of the dictionary to a text file, comma separated."""
    # empty check
    if not students:
        print('No student data to save.')
        return

    out_string = ''
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        line = f'{sid:d},{name:s},{score:d},{grade:s}'
        out_string += line + '\n'

    filename = 'dict2.txt'
    with open(filename, 'w') as savefile:
        savefile.write(out_string.rstrip('\n'))

    print(f'Data saved to {filename:s}')


def search():
    """Search for the student details matching student id entered by the user."""

    # empty check
    if not students:
        print('No student data to search in.')
        return
    # make a function, e.g  search_by_id()
    sid = int(input('Enter student id to search for >'))
    if sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        print(f'''
              Student ID:\t{sid:d}
              Name:\t\t{name:s}
              Score:\t\t{score:d}
              Grade:\t\t{grade:s}
              ''')
    else:
        print(f'No student with the id {sid:d} in our data.')

    # search by letter grade  (any non-key attribute)  ->  search_by_grade()
    grade_in = input('Enter grade to search for >').upper()
    found = False
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        if grade == grade_in:
            found = True
            print(sid, name, score, grade)  # improve
    # end for loop
    if not found:  # found == False
        print(f'No student has the grade {grade_in:s}.')


def compute_average():
    """Return average score from the dictionary.
       average for A grades as well 
    Also return the count of B grades and count of 100s (perfect scores) 
    """
    total_score = 0
    student_count = count_B = count_100 = 0
    total_for_A = 0
    count_A = 0

    for sid in students:
        student_details = students[sid]
        #name = student_details['Name']   << delete this line
        score = student_details['Score']
        grade = student_details['Grade']
        #update totals
        total_score += score
        student_count += 1
        if grade == 'A':
            total_for_A += score
            count_A += 1
            if score == 100:
                count_100 += 1
        elif grade == 'B':
            count_B += 1

    #end for loop
    if student_count > 0:
        avg = total_score / student_count
        #do the A avg here with an if
    else:
        avg = None
        #extra None here
    #end if

    return avg, count_B, count_100  #add the avg_A here. modify the call in summary.
    

def summary():
    """Use the average function and display average price, and high order count."""
    avg_score, count_B, count_100 = compute_average()
    if avg_score is not None:
        print(avg_score)
    else:
        print('No data for average score.')

    print(count_B, count_100)

def reset():
    """Empty out the dictionary."""
    global students

    students.clear() 


functions = {
            1: submit,
            2: load,
            3: display,
            4: save,
            5: search,
            6: summary,
            7: reset
             }

# main
while True:
    print('1.Submit 2.Load 3.Display 4.Save 5.Search 6.Summary 7.Reset 8.Quit')
    choice = int(input('Enter 1,2,3,4,5,6,7, or 8 >>'))

    if choice == 8:
        print("Poppin pills and sleeping in a cruh")
        break
    if choice not in functions:
        print('Invalid Choice')
        continue
    functions[choice]()
print("Poppin pills and sleeping in a cruh!")









'''
    print('1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit')
    choice = int(input('Enter 1,2,3,4,5 or 6 >>'))
    if choice == 1:
        display()
    elif choice == 2:
        save()
    elif choice == 3:
        search()
    elif choice == 4:
        summary()
    elif choice == 5:
        reset()
    elif choice == 6:
        break
    else:
        print('Invalid choice!')
print('Goodbye!')
'''