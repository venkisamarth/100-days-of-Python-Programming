#Globals()function 
#global() function return a dictionary  of current  globle  symbol table 
a=10 
def demo(): 
    print("hello")
print(globals())
print((globals()["a"]))

a=10
def demo(): 
    print("hello")
    print(globals()['a'])
    globals()['a']=1000
demo()
print(a)

a=20 
def demo(): 
    print("hello")
    b=1000
    print(locals() ["b"])
    globals()["a"]==1000
demo()
print(a)