import time 
class BankExceptionError(Exception): 
    pass 
class AttemptExceptionError(Exception): 
    pass 
attempts=1 
def withdrow(): 
    global attempts
    saved_pin=1234
    balence=10000
    pin=int(input('Enter the pin '))
    if pin==saved_pin: 
        try: 
            amt=float(input("Enter amount to witdrow"))
            temp_bal=balence-amt
            if temp_bal<1000: 
                raise BankExceptionError("insafficiant balance")
            balence=balence-amt
            print("Remained balnce is:",balence)
        except  Exception as var: 
            print(var)
    else: 
        ans=input("Do you want to continue again (y/n):")
    if ans.lower()=="y":
        attempts+=1 
        try: 
            if attempts==4: 
                raise AttemptExceptionError("Too many Attempts ,your account  is blocked for an hour")
        except Exception as var: 
            print(var)
            time.sleep(3600)
        else: 
            withdrow()
    else: 
        print("Think you !")
        return 
    withdrow()