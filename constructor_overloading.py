class Father: 
    def __init__(self): 
        print("Father constructor called")
        self.vehicle='scoter'

class Son(Father): 
    pass
s=Son()
print(s.__dict__)
class Father:
    def __init__(self): 
        print("Father constructor called")
        self.vehicle="Scotter"

class Son(Father):
    def __init__(self): 
        self.vehicle="BMW"
s=Son()
print(s.vehicle)
print(s.__dict__)