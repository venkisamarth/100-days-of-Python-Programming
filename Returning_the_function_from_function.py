def outer():
    def inner(): 
        print("hello")
    inner()
outer()
print("This is the call of the inner() function ")
a=10
def outer(): 
    def inner(): 
        print("hello world")
    inner()
    return a 
a=outer()
print(a)
print("##"*5)

def outer(): 
    a=10 
    def inner(): 
        print("hello world")
       
    return inner
inner=outer()
inner()

#Taking function  as input and returning function 
def Display(): 
    return 'helloworld'
def demo(f): 
    print(f())
    return f 
f1=demo(Display)
print(f1())

def outer_function(): 
    def inner_function():
        return "Hello from inner function"
    return inner_function

restul_function=outer_function()
print(restul_function())


# Returning a function with parameters: 
def outer_function(x):
    def inner_function(y): 
        return x+y 
    return inner_function
result_func=outer_function(5)
print(result_func(3))
# Returing the that captures varaibles from outer scope: 
def outer_function(x): 
    print(x)
    def inner_function(y): 
        return x+y
    return inner_function
restul_fun=outer_function(10)
print(restul_fun(3))

# Returing the a function with coditional logic 
def outer_function(): 
    def inner_function(x): 
        if x% 2==0: 
           return "Even"
        else: 
            return "Odd"
    return inner_function
result_func=outer_function()
print(result_func(4))
print(result_func(3))

#Returing different functions based on condtions 
def outer_function(choice):
    if choice == 'add':
        def add(x, y):
            return x + y
        return add
    elif choice == 'subtract':
        def subtract(x, y):
            return x - y
        return subtract

add_func = outer_function('add')
print(add_func(4, 2))  # Output: 6

subtract_func = outer_function('subtract')
print(subtract_func(4, 2))  # Output: 2

# Returing lambda function : 
def outer_function(): 
    return lambda x,y: x+y
result_func=outer_function()
print(result_func(4,3))

def outer_function():
    def inner_function(x=0):
        return x + 10
    return inner_function

result_func = outer_function()
print(result_func())  # Output: 10
print(result_func(5))  # Output: 15

#Retuirng a function that modifies a nonlocal varaible: 
def outer_function(): 
    count=0 
    def inner_function():
        nonlocal count
        count+=1
        return inner_function
restul_fun=outer_function()
print(restul_fun())
print(restul_fun())



        
            
