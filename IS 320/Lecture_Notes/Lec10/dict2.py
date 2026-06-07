'''
Name Adam
Score 90
Major IS

'''

student_details = {"Name": "Adam",
"Score": 90,
"Major": "IS"}

# print(student_details["Major"])
student_details.clear()

if not student_details:
    print("No data to display")
else:
    for attrib in student_details:
        value = student_details[attrib]
        print(attrib, value)

# student_details.clear()

# if not student_details:
#     print("No data to search")
# else:
#     attrib = input("enter atribute name >>")
#     if attrib in student_details:
#         print(student_details[attrib])
