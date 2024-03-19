print("this is the python class")
print('this is the normal file')
print("this cal be the more the file ")
num1=int(input("enter the first number "))
num2=int(input('enter the secod number'))
result=num1+num2 
print(result)

class student:
    collage="jain collage"
    def __init__(self,nm,m): 
        self.name=nm
        self.marks=m
std1=student("venki",99)
std2=student("raju",99)
std3=student("nami",88)
print(std1.name)
print(std2.marks)
print(std2.marks)