#the class which is delclared iside the another class or inside the another class is called nested class 
# when one class objects cannot exist without another object 
class outer: 
    def __init__(self): 
        def display(self):
            print("this is the class of the constructor called")
        class inner: 
            def __init__(self): 
                print("inner class constrocto called")
            def show(self): 
                print("This is show mehtod")
             # This is the program to print the natral numbers from 1 to 10 
# for i in range(10):
#         print(i)
            
obj1=outer()
in1=obj1.inner()
in1.show()
obj1.display()



