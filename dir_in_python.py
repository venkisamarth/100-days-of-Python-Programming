# In python ,dir() as a built-in  function that  return a list 
# all attributes (method,varaible and other attributes) for a given object
#
# dir(object)

x=100
my_name="shanthanu"
print(type(my_name))

# what are the methods we can apply on the my_list object 
# print(dir(my_name))

print("This is for x varaible")
print(dir(x))

# 1.special methods 
# 2.special attributes
# 3.normal metods and normal attributes


print(my_name.upper())
print(my_name.lower())

print(dir(x))
import man
print(dir(man))
print(dir(str))
print(dir())

x=10
def demo():
    print(dir(demo))

    print(type(demo))

    import math
    print(dir(math))

    print(math.sqrt(25))

    # How to find  variable and method when we run dir finction
    # dir() function
    print(math.sqrt(25))
    print(math.pi)

# reloding modules
    print("hello")
    import importlib
    importlib.reload(man)
    importlib.reload(man)
print(help("modules"))
# third party lib numpy
