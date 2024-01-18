# How to add multiple  value from the dict 

# adding multiple key_value  pairs 
# how to modify 
student={'raj':10000,"jay":20000}
print("before update:",student)
student.update({"jay":30000})
print("after update:",student)

# this overide the second element

student ={"raj":1000}
print("before adding :",student)
student.update({"jay":11000,"rohan":12000,"prjwal":140000})
print("after adding:",student)

# adding the multiple value usinng the mannal method 

n=int(input("enter  the number ood studnet: "))
for n in range(n):
    roll=int(input("enter the roll number of student"))
    marks=float(input("enter the marks {roll}"))
    if roll not in student:
        student[roll]=marks
    else:
        print("invalid roll number")

print("student data is:",student)




