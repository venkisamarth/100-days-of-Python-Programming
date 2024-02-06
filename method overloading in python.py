# when a class contain two o more methods with same name but diffrent bahavior is called as method oveloading  
class Addtion: 
    def add(self,num1,num2): 
        print("additions is:",num1+num2)
    def add(self,num1,num2,num3): 
        print("addtion is:",num1+num2+num3+num3)
a=Addtion()
a.add(10,20,30)
