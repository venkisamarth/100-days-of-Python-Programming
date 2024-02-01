# #non local varaible in oython are varaible that are refrence 
# def outer(): 
#     count =0 
#     def inner(): 
#         nonlocal count 
#         count+=1 
#         print("count inside inner funcion:", count )
#     inner()
#     print("count outside inner function : ", count )
# outer()

# # Access and modify a non local variable from an outer fucntion 
# def outer(): 
#     count =0 
#     def inner(): 
#         nonlocal count 
#         count+=1
#         print("count inseide inner function: ", count ) 
#     inner() 
#     print("count outside inner function: ",count)
# outer()
# print("count the outer inner function with the normal :",outer)        

# # using a non local varaible a in a recursion function 
# def outer(): 
#     count= 0 
#     def inner(): 
#         count +=1 
#         print("count inside inner function :",count)
#     inner()
#     print('count outside inner function:',count)
# outer()


# #using a nonlocal varaible in a recursive fuction 
# def outer(): 
#     count=0 
#     def inner(): 
#         nonlocal count 
#         count +=1 
#         if count <5: 
#             inner()

#     inner()
#     print("Final count:",count )
# outer()
# example 1 
def outer_function(): 
    x=10 
    def inner_function(): 
        nonlocal x 
        x+=5 
        print("Inner function")
    inner_function()
    print("outer function")
outer_function()

# Example 2 
def outer_function(): 
    x=10 
    def inner_function(): 
        nonlocal x 
        x*=2
    inner_function()
    print("outer function:",x) 
outer_function()
# example 3 
def outer_function(): 
    x=10 
    def inner_function(): 
        nonlocal x 
        x-=3
        print("Inner function:",x)
    inner_function()
    print("Outer function:",x)
outer_function()
#example 4 
def outer_function(): 
    x=[1,2,3,4]
    def inner_function(): 
        nonlocal x 
        x.append(4)
        print("inner function:",x)
    inner_function()
    print("outer Function:",x)
outer_function()

# example 5 
def outer_function(): 
    x={"a":1,"b":2}
    def inner_function(): 
        nonlocal x 
        x['c']=3 
        print("inner function:",x)
    inner_function()
    print("outer function:",x)
outer_function()

def outer_function(): 
    x=10 
    def inner_function(): 
        nonlocal x 
        x/=2 
        print("inner function:",x)
    inner_function()
    print("outer function:",x)
outer_function()
#example 7 
def outer_function(): 
    x=10 
    def inner_function(): 
        nonlocal x 
        x//=2 
        print("inner function:",x)
    inner_function()
    print("outer function:",x)
outer_function()
# Example 8
def outer_function(): 
    x=10 
    def inner_function(): 
        nonlocal x
        x**=2 
        print("Inner function:",x)

    inner_function()
    print("outer function:",x)
outer_function()

# example 9 
def outer_function():
    x="Hello"
    def inner_function(): 
        nonlocal x
        x+="world!"
        print("innter Function :",x)
    inner_function()
    print('the outer function:',x)
outer_function()

# exmaple 10 
def outer_function(): 
    x=True
    def inner_function(): 
        nonlocal x 
        x=not x 
        print("Inner Function:",x)
    inner_function()
    print("outer function:",x)
outer_function()




