# what are callable objects? 
# the function can be called whenver required  
# objects having __call__() method in their

# function are calleable 

x=100 
def add(a,b): 
    return a+b 
print(type(add))
print(callable(add))
print(callable(x))
print(add(10,20))
print(add.__call__(10,20))

class  Add(object): 
    def __init__(self,a,b): 
        self.a=a
        self.b=b 
a1=add(10,20)
print(callable(add))
print(callable(a1))
# how make objects as callable 
def __call__(self): 
    print("hello")
a1=add(10,20)
def __all__(self,a,b): 
    return a,b 

a=add(10,20)
a=add(10,20)
print(a(10,20))
print(callable(a))
print(a1(100,300))