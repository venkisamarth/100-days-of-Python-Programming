class Person: 
    def __init(self,nm,age):
        self.name=nm
        self.age=age
class Employee(Person): 
    def __init__(self,sal): 
        self.salary=sal
class student(Person): 
    def __init__(self,nm,ag,m):
        
        self.marks=m

s1=student("jay",21,90)
