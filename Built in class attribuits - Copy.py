# __dict__ dictionary containg clsss names 
# __doc__ class documentation string 
# __name__ class name 
# __module__ module name  in which class is defined 
# __bases__ list of base class 

class Employee: 
    "This is Employee class for maintaing employee data"
    def __init__(self,nm,ag): 
        self.name=nm
        self.age=ag
    def display(self): 
        print(f'name is {self.name} and age {self.age}')

e1=Employee("jsy",21)
e2=Employee("venki",25)
print(Employee.__dict__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__class__)

print(Employee.__module__)
