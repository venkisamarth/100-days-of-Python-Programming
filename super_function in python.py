#using super() funtion we can acess parent class
class computer: 
    def __init__(self): 
        self.ram="8gb"
        self.storage="512gb"
        print("computer class costructor called")
class Mobile(computer): 
    def __init__(self): 
        super().__init__()
        self.model="iphone"
        print("mobile class constructor called")
Apple=Mobile()
print(Apple.__dict__) 


class computer(object): 
    def __init__(self,ram,storage): 
        self.ram=ram
        self.storage=storage
        print("computer class constructor called")
class Mobile(computer): 
    def __init__(self,ram,storage): 
        self.model="iphonex"
        print("mobile class costructor called")
Apple=Mobile('8gb','512gb')
print(Apple.__dict__)
def display(self): 
    print("hello world ")

Apple=Mobile("8gb","512gb")
print(Apple.__dict__)
