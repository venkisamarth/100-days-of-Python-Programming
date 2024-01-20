student ={}
n=int(input("enter the number of student to update"))
for i in range(n):
    name=input("ente the name of the student: ")
    marks=int(input("enter the marks obtained by the student:  "))
    student[name]=marks
    ans=input("do you want to containue (y/n)")
    if ans !="y":
        break
print(student)
