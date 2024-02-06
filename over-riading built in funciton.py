# class cart : 
#     def __init__(self): 
#         print("This is cart object ")
# c1=cart()
# print(c1)

class Cart : 
    def __init__(self,basket1,basket2,basket3): 
        self.colthes=basket1
        self.electronics=basket2
        self.other=basket3

    def __len__(self): 
        print("Total number of items in cart :")
        return len(self.colthes)+len(self.electronics)+len(self.other)
    
shanathnu=Cart(['pant','shirt','t-shirt'],['eirphine','phone','microphone'],["chairs"])
print(len(shanathnu))

