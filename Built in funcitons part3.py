print("Strings funcitons in python ")
#Creating a string 
my_string ="hello,world"
#Concatination  strings : 
strings1 ="Hello"
strings2="world"
combained_string=strings1+"  "+strings2
print(combained_string)

print("sum function in python ")
#sum of numbers in a list 
numbers=[1,2,3,4,5]
total=sum(numbers)
print(total)

print("the sum of numbers using  sum() function ")
result=sum(10,20)
print(result)

print("sum of numbers enterd by the users:")
num1=int(input("Enter first numbers"))
num2=int(input("Enter the numbers: "))
total=num1+num2
print("The sum is: ", total)

print("sum of range of numbers ")
total=sum(range(1,11))
print(total)

print("The sum of elements in tuple:")

my_tuple=(1,2,3,3,4)
sum_tuple=sum(my_tuple)
print(total)


print("super() funciton")
class ParentClass: 
    def __init__(self): 
        print("ParentClass __init__ called.")
class ChildClass(ParentClass): 
    def __init__(ParentClass): 
        super().__init__()
        print("ChildClass __init__ called.")
Child_obj=ChildClass()

print("using multiple inheritance")
class Parent1: 
    def show(self): 
        print("Parent1")
class Parent2: 
    def show(self):
        print("Parent2")

class Child(Parent1,Parent2): 
    def show(self): 
        super().show()
child_obj=Child()
child_obj.show()

#Accessing parent methods 

class Parent: 
    def show(self):
        print("parent method")
class child(Parent): 
    def show(self): 
        super().show()

child_obj=child()
child_obj.show()

         

