#To overload method we used to write methods logic so that diffrent code execution 
#inside the method according to parameters provided
class claci: 
    def add(slef,num1,num2,num3): 
        if num1!=None and num2!=None and num3!=None: 
            print("The Addition is :",num1+num2+num3)
        elif num1!=None and num2!=None: 
            print("Addtion is:",num1+num2)

        else: 
            print("incorect parameters provid")

c1=claci()
# c1.add(10,20)
c1.add(10,20,30)
c1.add(10,20,30)

class Area: 
    def area(self,l=0,b=0): 
        if l>0 and b>0: 
            print("area of reactange is :",l*b)
        elif l>0 and b==0: 
            print("area pf square is:",l*l)
a=Area()
a.area(2,9)
a.area(10,10)


        


