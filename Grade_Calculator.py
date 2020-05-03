"""
User requirements:
1. Teacher wants to enter the marks of a student
2. from the marks entered, calculate grade
3. After entering multiple students then calculate average pass percent of a whole class

Tasks:
add_student
    1. get the user input(name) as parameter
    2. check if the student already exists
        i. if exists then dont add the student return (name,ALREADYEXISTS)
        ii. if doesn't exists then add the student return (name,NEWLYADDED)

add_subjects
    1. get the userinput - stud name
    2. check student exists
        i. if already exists then add the subjects
        ii. if doesnt exists then throw error
    3. finally
add_marks
calculate_grade
    1. add_student() if doesnt exist
    2. add_subjects()
    3. add_marks()
    4. decide pass or fail
    5. if passed then calculate
calculate_average_passpercent
"""
def add_student(addstud_name):
    studname, status = get_student(addstud_name)
    if status == "EXISTS":
        print("Student name - {} {}".format(studname,status))
    elif status == "NOTEXIST":
        print("Student name - {} not exists".format(addstud_name))
    else:
        print("unknown error")

def get_student(getstud_name):
    if getstud_name in Class_register:
        return getstud_name,"EXISTS"
    else:
        return getstud_name,"NOTEXIST"

Class_register = ["Saran", "Jana", "HemaKumar", "Danny","Rocky"]

userinput_studname = str(input("Enter the student name to check: "))
add_student(userinput_studname)

