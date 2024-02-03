#This is used for check the object belongs particuler function
class Demo: 
    pass
d1=Demo()
class Employee: 
    "This is Employee class for maintaing employee data"

    def __init__(self,nm,ag): 
         self.age=ag
         self.name=nm
    def display(self): 
           print(f"The name is {self.name} add the age is {self.age}")
e1=Employee("jay",23)
e2=Employee("raj",23)

print(isinstance(e1,Employee))
print(isinstance(e2,Employee))
print(isinstance(d1,Employee))

# if isinstance(obj,clssname): 
#      pass
