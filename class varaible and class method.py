class Student: 
    def __init__(self,nm,m): 
         self.name=nm 
         self.marks=m
std1=Student("venki",90)
std3=Student("raju",90)
std3=Student("Ram",90)
# class varaibles 
#variabls mode for entire class (all objects )
#only one copy is created and distributed to all objects 
# modifictaion in class vraible impact on all objects 
class Employee: 
     company_name='infosys'
     def __init__(self,nm,sal): 
          self.name=nm
          self.salary=sal
e1=Employee("jay",230000)
e2=Employee("vijay",23000)
# how to access the  
print(Employee.company_name)
print(e1.company_name)
print(e2.company_name)
print('How to modify the clss variables')
Employee.company_name="TCS"
print(Employee.company_name)
print(e1.company_name)
print(e2.company_name)
e2.company_name="TCS"
print(Employee.company_name)

# class mehtod 
# class method works on class varaible 
# First  argumetns is class referance 
# class referance 

# made using decoraters @classmethod 

class Employee: 
    company_name='TCS'
    def __init__(self,nm,sal): 
          self.name=nm
          self.salary=sal 

    @classmethod
    def get_comapy_name(cls): 
        cls.company_name="TCS"
        print(f"company name is:",cls.company_name)
        print(cls.company_name)

e1=Employee("jay",3000)
e2=Employee("vijay",5000)
Employee.get_comapy_name()
print(e2.company_name)


        
        

