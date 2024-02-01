def my_decorator(fun): 
    def wrapper(): 
        print("somthing is happening before the function is called: ")
        fun()
        print("Somethig is happening after the function is called :")
    return wrapper
@my_decorator
def say_hello(): 
    print("Hello!")
say_hello()

#example 2 
def my_decorator(func): 
    def wrapper(name): 
        print("Something is happening before the function is called: ")
        func(name)
        print("Something is happeng after the function is called :")
    return wrapper
@my_decorator
def greet(name): 
    print("Hello,",name)
greet("Alice")

print("##"*2)
def repeat_twice(func): 
    def wrapper(): 
        func()
        func()
    return wrapper
@repeat_twice
def greet(): 
    print("Hello!")
greet()

print("##"*4)

# example 4 
def uppercase(func): 
    def wrapper(*args,**kwargs): 
        result =func(*args,**kwargs)
    return wrapper
@uppercase
def greet(name): 
    return f"Hello,{name}"
print(greet("Alice"))


