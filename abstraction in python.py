#Hiding complex imlimentation  from the user is called  abstraction 
# send butten 
# atm interface 
# by using moduel :abc 
# interface calls from abc callss 
# create abstraction  methods in your abstraction calls 
# class Employee(ABC): 
#     #abstraction 
#     #concreate method 

from abc import ABC,abstractclassmethod 
class car(ABC): 
    @abstractclassmethod
    def milege(self): 
        pass 
    def color(self): 
        print('white')
class maruti_suzuki(car): 
    def milege(self): 
        print("milage is 30 kmph")
class Dustuster(car): 
    def milage(self): 
        print('milage is 35 kmph')
class TATA(car): 
    def milage(self): 
        print("milage is 40 kmph")
m1=maruti_suzuki()
t1=TATA()
d1=Dustuster()
t1.milage()





