# Types of varaible 
# instace varaible 
# class varaible 

# instace varaible 

class student: 
    def __init__(self,nm,m): 
        self.name=nm
        self.marks=m

std1=student('venki',90)
std2=student("raju",99)

std3=student("nemi",89)
# Instance 
# Variable made for paraticuler instance 
# separate copy is created for Every  object 
# values of varaibles differs form object to object 
# modification of the one object won't effect the another object 
class student: 
    def __init__(self,nm,m): 
        self.name=nm
        self.marks=m
std1=student("Akshay",89)
std2=student("raj",89)

print(std1.__dict__)
print(std2.__dict__)

print(std2.name)

# creating the instance variable 

# using constroctor varaible 
# using instance method 
# outside class 

# instance  method()

class student: 
    def __init__(self,nm,m): 
        self.name=nm
        self.marks=m 

    def display(self): 
        print(f"{self.name},{self.marks}")

    def change_data(self): 
        self.name=input("enter the name")
        self.marks=input("Enter the marks")
std1=student("akshay",89)
std2=student("Raj",89)

std3=student("jay",80)

std1.display()
std2.display()

std1.change_data()
print(std1.__dict__)