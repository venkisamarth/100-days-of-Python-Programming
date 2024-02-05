#what is Encapsulation  in python 
# Need of Encapsulation in python 
# Acess Modification in python 
#Name mangling in concept 
#making private method 

#Encapsulation in python 
#wraping up data and methods working on data together in single unit is called as encapsulation 

class Employee: 
    def __init__(self,nm,sal): 
        self.name=nm
        self.salary=sal
    def display(self): 
        print(f"name is :{self.name}and salary is {self.salary}")
class Finace: 
    def __init__(self): 
        self.revenue=10000
        self.number_of_sales=144
f1=Finace()
print(f1.__dict__)
class HR: 
    def __init__(self): 
        self.number_of_sales=32
        f1.revenue=1 
        print(f1.revenue)

h1=HR()
print(f1.__dict__)
#Encapsulation restrict  the modificaton of the data outside the class in encapsulation
#Gneeraly we restrict data acess outside the class in encapsulation 
# Generaly we restrict data acess outsid the clas in encapsulation 

#Encapsulationn ca be acived be declaring  the data members and methods of a class as private
#There acess specification :- public provate private 

#public member 
#acessible any where by using object refernce 
#private member :- accessible within the class accesible via method only 
# protectd member : -  acessible within class and its subclass 
class Finace: 
    def __init__(self): 
        self.__revenue=100000
        self.__number_of_sales=144
f1=Finace()
print(f1.__dict__)
class HR: 
    def __init__(self): 
        self.number_of_sales=32
        # print(f1.__revenue)
        f1.__revenue=0 
        # print(f1.__revenue)
hr=HR()
print(f1.__dict__)
class Finace:
    def __init__(self): 
        self.__revenue=1000
        self.__number_of_sales=144
    def display(self): 
            print(f"revenue is :{self.__revenue} and number of sales :{self.__number_of_sales}")
            self.__revenue=20000
            print(f"revenue is :{self.__revenue} and number of sales :{self.__number_of_sales}")
f1=Finace()
f1.display()
print(f1.__dict__)
# using method only we can modify and access private varaible
