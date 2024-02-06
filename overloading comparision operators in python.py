# class Hotel: 
#     def __init__(self,name,fare): 
#         self.name=name
#         self.fare=fare
#     def _get_(self,other): 
#         return self.fare>other.fare
    
# h1=Hotel("Taj Hotel",2000)
# h2=Hotel("panchatantra",10000)
# print(h1>h2)
class Book: 
    def __init__(self,title,pages): 
        self.title=title
        self.pages=pages
    def __add__(self,other): 
        total=self.pages+other.pages
        return Book("All books ",total)
    def __str__(self): 
        return str(self.pages)
    
b1=Book("one indian girl",300)
b2=Book("making india awsome",400)
b3=Book("half girl firends",400)
b4=Book("girl in 105 room",300)
print("totle number os pages",b1+b2+b3+b4)

    

