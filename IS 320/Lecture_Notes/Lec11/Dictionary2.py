"""
This global dictionary contains order id:order price pairs.

"""

students = {
    1001: {'Name':'Alex', 'Score': 100, 'Grade': 'A'},
    1002: {'Name': 'Alex', 'Score': 77, 'Grade': 'B'},
    1003: {'Name': 'Denise', 'Score' : 90, 'Grade' : 'A'},
    1004: {'Name': 'Emily', 'Score' : 40, 'Grade': 'B'}
    }

# functiions

def display():
    """Show the contents of the dictionary."""
    if not students:
        print("No student data to display.")
        return

    width = 46
    line = '-' * width
    print(line)
    print(f'|{"Student ID":<12s}|{"Name":^15s}|{"Score":^7s}|{"Grade":^7s}|')
    print(line)
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        
        print(f'|{sid:<12d}|{name:^15s}|{score:^7d}|{grade:^7s}|')
    print(line)


def save():
    """Save the contents of the dictionary to a text file, comma separated."""
    if not students:
        print("No student data")
        return

    out_string = ''
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        line = f'{sid:d}, {name:s}, {score:d}, {grade:s}'
        out_string += line + '\n'

    filename = 'dict2.txt'
    with open(filename, 'w') as savefile:
        savefile.write(out_string.rstrip('\n'))
    print(f'Data saved to {filename:s}')


def search():
    """Search for the price matching order id entered by the user."""
    if not students:
        print("No student data to search")
        return
    sid = int(input('Enter Student ID to search for >>>'))
    if sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        print(f'''
              Stewie ID:\t{sid:d}
              Name:\t\t {name:s}
              Score:\t\t {score:d}
              Student:\t\t {grade:s}
              ''')
    else:
        print("cruh pick a right student")

    grade_in = input("enter grade to search for >>>")
    found = False
    for sid in students:
        student_details = students[sid]
        name = student_details['Name']
        score = student_details['Score']
        grade = student_details['Grade']
        if grade == grade_in:
            found = True
            print(sid, name, score, grade)
    if not found:
        print('No student has the grade')



def compute_average():
    """Return average order price from the dictionary.

    Also return the count of orders with price above 200.00
    """
    total_score = 0
    student_count = count_B = count_100 = count_A = 0
    total_for_A = 0
    for sid in students:
        student_details = students[sid]
        score = student_details['Score']
        grade = student_details['Grade']
        total_score += score
        student_count += 1
        if grade == 'A':
            total_for_A += score
            count_A += 1 
            if score == 100:
                count_100 += 1
        elif grade == 'B':
            count_B += 1

        if student_count > 0:
            avg = total_score / student_count
            if count_A > 0:
                a_avg = 
        else:
            avg = None

    return avg, count_B, count_100


def summary():
    """Use the average function and display average price, and high order count."""
    avg_score, count_B, count_100 = compute_average()
    if avg_score is not None:
        print(avg_score)
    else:
        print("No data")
    print(count_B, count_100)


def reset():
    """Empty out the dictionary."""
    global students
    students.clear()



# main
quit = False
while not quit:
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
        print("Data Cleared")
    elif choice == 6:
        quit = True
    else:
        print('Invalid choice!')
print('Goodbye!')

"""
Results of running the program:

1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>1
-----------------------
|    ID    |  Price   |
-----------------------
|1001      |    150.00|
|1002      |    250.00|
|1003      |    300.00|
|1004      |    200.00|
|1005      |    100.00|
-----------------------
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>2
Data saved to dlab1.txt.      <<- Contents of saved file -scroll to end.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>3
Enter order ID to search for >>1004

        Order ID        :1004
        Order Price     :200.00
        
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>3
Enter order ID to search for >>1010
No order with ID 1010.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>4

        Average Price           :200.00
        High Order Count        :2
        
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>5
Orders reset.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>1
No orders to display.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>2
No orders to save.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>3
No orders to search in.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>4
No orders for average and count.
1.Display 2.Save 3.Search 4.Summary 5.Reset 6.Quit
Enter 1,2,3,4,5 or 6 >>6
Goodbye!

Contents of saved file:
1001,150.00
1002,250.00
1003,300.00
1004,200.00
1005,100.00
"""
