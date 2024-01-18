

student ={}
n=int(input("enter how many student to add?: "))
while len(student)<n:
    roll=int(input("enter the roll number of student:"))
    marks=float(input(f'enter the marks of {roll}:'))

    if roll in student:
        student[roll]=marks
    else:
        print("invalid roll number")
print('student data is:',student)