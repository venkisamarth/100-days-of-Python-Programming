class  Veh: 
    def __init__(self,name,color,price): 
        self.name=name
        self.color=color
        self.price=price
    def get_details(self): 
        print("name of is:",{self.name})
        print("color is :",{self.color})
        print("price is :",self.price)

    def max_speed(slef): 
        print("gear change is 6 ")

class car: 
    def max_speed(self): 
        print("maximum speed limit is 140")
    def gear(self): 
        print("gear change is 7")
V1=Veh("Truck","red",200000)
c1=car("Car","white",700000)
V1.get_details()
c1.get_details()
V1.max_speed()
c1.max_speed()