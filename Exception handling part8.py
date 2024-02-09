point_table={"india":8,
             "pakistan":3,
             "south Africa":5,
             "Bangladesh":4,
             "neterland":2,
             "Bremuda":2 
             }
while True: 
try: 
    name=input("Enter the country name")
    points=points_table[name]
    print(f"{name} has got {points} points")
except: 
    print("No such country")
else: 
    break