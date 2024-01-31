#a function calls itself  then that function is called asd recursion function the process is called as recursion 
i=0 
def demo(): 
    global i 
    print("hello")
demo()

#maximum recursion depth exceeds while calling a python  a python object 
import sys 
print(sys.recursionlimitlimit())
sys.setrecursionlimitlimit(200)
print(sys.getrecursionlimit())
def demo(): 
    global i 
    i=i+1 
    print("hello")
    demo()

# demo()
# advantages of the recursion function 
# clean code 
# complex problems can be sloved essy 
# disadvantages 

# hard to debugging 
# not memeory efficency



