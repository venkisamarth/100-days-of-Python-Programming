student={}
n=int(input("How many student to add?:"))
while True:
    roll=int(input("enter the roll number of student:"))
    marks=float(input("enter the marks of {roll}:"))
    if roll not in student:
        student[roll]=marks
    else:
        print('alredy exist')
    ans=input("Do you want to continue?(y/n)")
    if ans!="y":
        break
print("student data:",student)


