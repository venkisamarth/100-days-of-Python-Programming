# What is constructor?
# it is special method withinn a class that is autometically called when a new instance of the class is created when  
# it is used to initialize the object's attributes or perform any necessary setup tasks 

# Types of constructor in python 
# parameterised constructor 
# non parameterised constructor 
# default constructor


#1 parameterised constroctor 

class Employee: 
    def __init__(self,nm,ag): 
        self.name=nm
        self.age=ag
    def display(self): 
        print(f"name is {self.name}and the age is{self.age}")
e1=Employee("venki",23)
e2=Employee("raju",24)
print(e1.name)
print(e2.name)
print(e1.age)
print(e2.age)
print(e1.__dict__)
print(e2.__dict__)
e1.name="venkisamarth"
print(e1.name)

# non parameterized constroctor

class Employee: 
    def __init__(self): 
        self.salary=230000
        self.age=21
e1=Employee()
e2=Employee()
print()
        
# default constructor

class Employee: 
    pass
e1=Employee()
e2=Employee()

print(type(e1))
print(type(e2))


