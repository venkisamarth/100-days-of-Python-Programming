#sorted
# staticmethod
# str
# sum
# super

print("staticmethod():")
class myClass: 
    @staticmethod
    def my_statci_method(x): 
        return x*2 
obj=myClass()
print(obj.my_statci_method(7))

class MathOperations: 
    @staticmethod
    def add(x,y):
        return x+y 
obj1=MathOperations()
print(obj1.add(3,6))

class StringOperatins: 
    @staticmethod
    def reverse(string): 
        return string[::-1]
obj2=StringOperatins()
print(obj2.reverse("venkatesh"))

class UtilityFunction: 
    @staticmethod
    def is_even(num): 
        return num%2==0 
obj3=UtilityFunction()
print(obj3.is_even(5))

class Convertor: 
    @staticmethod
    def feet_to_inches(feet): 
        return feet * 12 
obj4=Convertor()
print(obj4.feet_to_inches(34))

class Validator: 
    @staticmethod
    def is_palindrom(string): 
        return string==string[::-1]
result=Validator.is_palindrom("venki")
print(result)

print("str()")
# Example 1 
my_int=42 
my_str=str(my_int)
print(my_str)

my_float=3.14
my_str=str(my_float)
print(my_str)

my_list=[1,2,3,4,4]
my_str=str(my_list)
print(my_str)

my_dict = {'a': 1, 'b': 2}
my_str = str(my_dict)
print(my_str)

my_bool =True
my_str=str(my_bool)
print(my_str)

print("sum funciton in python ")
my_list=[1,2,3,4,5]
restult1=sum(my_list)

my_tuple=(10,20,30)
result2 =sum(my_tuple)
print(restult1)
print(result2)

result4=sum({1,2,3})
print(result4)

result5=sum((x * 2 for x in range(1,6)))
print(result5)

print("super()")
class ParentClass: 
    def display(self): 
        print("ParantClass method")
class ChildClass(ParentClass): 
    def display(self):
        super().display()
        print("childClass method")


obj1 =ChildClass()
obj1.display()

# Example 2 
class AnotherChildClass(ParentClass):
    pass 
obj2=AnotherChildClass()
obj2.display()

# Example 3 
class GrandChildClass(ChildClass): 
    def dispplay(self): 
        super().display()
        print("GrandChildClass method")
obj3=GrandChildClass()
obj3.display()

class GrandGrandChildClass(GrandChildClass): 
    pass 
obj4=GrandChildClass()
obj4.display()








    