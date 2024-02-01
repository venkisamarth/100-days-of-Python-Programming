#example 1 
def outer_function(x): 
    def inner_function(y): 
        return x + y 
    return inner_function
closure=outer_function(5)
print(closure(3))

#example 2 
def outer_function(message): 
    def inner_function():
        print(message)
        return inner_function
closure=outer_function("Hello, function!")
# print(closure())
#example 3 
def outer_function(x): 
    def inner_function():
        return x 
    return inner_function
closure=outer_function(10)
print(closure())

#example 4 
def outer_function(x):
    def inner_function(y): 
        return x*y
    return inner_function
closure=outer_function(5)
print(closure(3)) 

#example 5 
def outer_function(): 
    count=0 
    def inner_function(): 
        nonlocal count
        count+=1 
        return count 
    return inner_function
closure=outer_function()
print(closure())
print(closure())

#example 6 
def outer_function(): 
    message="Hello from outer function"
    def inner_function(): 
        print(message)
    return inner_function
closure=outer_function()
closure()

def outer_function(x): 
    def inner_function(y): 
        return x+ y
    return inner_function
closure=outer_function(5)
closure2=outer_function(10)

print(closure(3))
print(closure2(3))

def outer_function(x): 
    def inner_function(y): 
        return x*y
    return inner_function
double=outer_function(2)
triple=outer_function(3)
print(double(5))
print(triple(5))

#example 6 
def outer_function(): 
    message="Hellp from outer function"
    def inner_function(): 
        print(message)
    return inner_function
closure=outer_function()
closure()

# example 7 
def outer_function(x): 
    def inner_function(y): 
        return x+ y 
    return inner_function

closure1 =outer_function(5)
closure2 =outer_function(10)
print(closure1())
print(closure2())

# example 
def outer_function(x): 
    def inner_function(y): 
        return x+y 
    return inner_function
closure1 =outer_function(5)
closure2=outer_function(10)
print(closure2(3))
print(closure1())









