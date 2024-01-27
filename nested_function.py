#Example 1: Simple nested function 
def outer_function(): 
    def inner_function():
         print("This is the inner funcion")

    print("Outer function")
    inner_function()
outer_function()

#Example 2: Returning a nested function 
def outer_function():
     def inner_function():
          return "inner function"
     return inner_function
fn=outer_function()
print(fn())

#Example 4: Passing  argument  to nested  function 
def outer_function(): 
    def inner_function(flag):
        if flag:
            print("Flag if True")
        else:
            print("Flag is False")
    inner_function(True)

outer_function()

        

