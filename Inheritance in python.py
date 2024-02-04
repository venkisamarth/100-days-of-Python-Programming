#deriving the new class from the existing class  so that new class inheritance all members (aattributes amd methods) of existing clsss is called as inheritance 
class Employee:
     bonus=2000
     def display(self): 
          print("This is the employee class method:")
class Manager(Employee): 
     bonus1=50000
     def show(self): 
          print('This is the manager class mehtod')
e1=Employee()
m1=Manager()
print(e1.display())
print(m1.show())
print(m1.bonus)
print(m1.bonus)

m1.display()
print(m1.display)
# e1.show()
