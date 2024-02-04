class country: 
    office="Delhi"
class State: 
    office="Mumbai"
class District(State,country): 
    pass
d=District()
print(d.office)
class country: 
    def __init__(self): 
        print("country class contstruct")
        self.office="Delhi"
class state: 
    def __init__(self): 
        super().__init__()
        print("State class constructor")
        self.office="Mubmbi"
class District(): 
    def __init__(self): 
        
        print("District class constructor")
        self.office="pune"

d=District()
print(d.__dict__)