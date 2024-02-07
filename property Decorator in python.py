class Employee: 
    def __init__(self,first,last): 
        self.first_name=first
        self.last_name=last
        self.mail=first+last
    def function(self): 
        return f"{self.first_name}{self.last_name}"
e=Employee("shantanu","keshakar")
e1=Employee("venki","venkatesh")
e2=Employee("raju","naikerr")

print(e.first_name)
print(e.last_name)
print(e.mail)
print("This is the second object  infirmation")
print(e1.first_name)
print(e1.last_name)
print(e1.mail)

# Need of property decorater 
def __init__(self,first,last): 
    self.firstname=first
    self.lastname=last

@property
def mail(self):
    return f"{self.firstname}{self.lastname}@gmail.com"
@property
def fullname(self): 
    return f"{self.firstname}{self.lastname}"

e=Employee('shantanu',"kejkar")
e2=Employee("venki","raju")
print(e.first_name)
e.first_name="raju"
print(e.first_name)

