class student: 
    def __init__(self,name,roll,dd,mm,yy): 
        self.name=name
        self.roll=roll
        self.dob=self.DOB(dd,mm,yy)
    def display(self): 
        print(f'name is{self.name}and roll is {self.roll}')
        self.dob.display()
class DOB: 
    def __init__(self,dd,mm,yy): 
        self.date=dd 
        self.month=mm
        self.year=yy

    def display(self): 
        print(f"Date of birth is:{self.date}/{self.month}")

s1=student("ajay",101,26,3,1999)
s1.display

    