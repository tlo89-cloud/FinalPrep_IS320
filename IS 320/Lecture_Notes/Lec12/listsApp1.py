# intro to lists

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
            process_line(line)

load()
print(students)
submit()
