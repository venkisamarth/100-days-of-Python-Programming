class BMW: 
    def fuel_type(self): 
        print("Disel")
    def max_speed(self): 
        print("max speed is 200")
class Ferrari: 
    def fuel_type(self): 
        print("petrol")
    def max_speed(self): 
        print("max speed is 180")
def car_details(object): 
    object.fuel_type()
    object.max_speed()

bmw=BMW()
ferrari=Ferrari()
car_details(bmw)
car_details(ferrari)