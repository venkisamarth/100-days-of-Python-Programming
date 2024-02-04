# instance methods 
#setter method =set value of instance variable 
#getter method =set value of instance variable

class Employee: 
    def setName(self,nm): 
        self.name=nm 
    def getName(self): 
        print("The name is :",self.name)
e1=Employee()
e2=Employee()
e1.setName(input("Enter the name:"))
e2.setName(input("Enter the name:"))
print("e1 object is :",e1.__dict__)
print("e2 object is:",e2.__dict__)
