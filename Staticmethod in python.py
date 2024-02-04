# Types of methods 
#   isinstance method 
#   class method 
#   staticmethod 
#methods which performs operation on external data 
# It can also perform operations on class data 
# no need to pass object or class referance 
# created using decorated @staticmethod 
class Bank: 
    bank_name="BOI"
    rate_of_interest=12.25
    @staticmethod
    def simple_interest(prin,n): 
        si=(prin*n*Bank.rate_of_interest)/100
        print("The simpl interest is:",si)
prin=(float(input("Enter the principle amount:")))
n=int(input("enter  number of years: "))

Bank.simple_interest(prin,n)



