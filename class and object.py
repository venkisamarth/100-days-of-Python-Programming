# # class-classis template /blueprint/prototype for creating the objects 
# # Every objects belongs to some class 
# # example email class as template of blue print 
# Why we call call as template or blue print 
# Attribute:-
# heading 
# participaents 
# attachmetns 

# methods 
# send 
# save_as_draft 

# email1 
# heading= taking leave 
# participaents=xys
# attachments =from pdf 
# class is a collection of Attribute and the methdos 
# class is the a collection of the objects 
# Thechincally Class is user defined data type 
x=100
print(type(x))
def demo(): 
    print("hello")
print(type(demo))
demo()

# what is class 

# creating class and object  
# class class_name: 
#     # attributes 
#     # methods 

# obj1= class_name([args])
# obj2=class_name([args])
class Email: 
    pass 
obj1=Email()
obj2=Email()
print(Email.__dict__)
print(type(obj1))
print("***"*5)

class Employee: 
    def __init__(self,nm,ag): 
        self.name=nm
        self.age=ag
    def display(self): 
        print(self.name,self.age)

e1=Employee('venki',21)
e2=Employee('raju',23)
print(type(e1))
print(type(e2))
print(e1.age)
print(e2.age)
print(e1.name)
print(e2.name)
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)