class Book: 
    def __init__(self,title,pages): 
        self.title=title
        self.pages=pages
b1=Book("one indian girl",3000)
b2=Book("making india awsome,",2000)
print("total number of pages :",b1.pages+b2.pages)
# print("The total numer of pages on are:",b1+b2)

class Book: 
    def __init__(self,title,pages): 
        self.title=title
        self.pages=pages
    def __add__(self,other): 
        total=self.pages+other.pages
        return total
b1=Book("one indian girl",3000)
b3=Book("The boyes adda",200)
print("The total pages are: ",b1+b2)


