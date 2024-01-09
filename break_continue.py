# In python break and continue statments  used to alter the flow  of program
# when break occurence control of program body of loop 
# sysntax  
# for var in sequnce:
#     # code inside for loop 
#     if condition:
        # break 
    #code inside loop 
    # rest of statments
# while loop 
# while codition :
#     # code inside while loop 
#     if condtion:
#         break 
#codes inside 
# printing first 10 numbers 
# i=1
# while  i<=10:
#     if i==5:
#         break 
#     print(i)
#     i+=1
# name=input("enter name:")
# for char in name:
#     if char =='t':
#         break 
# print(char,end=" ")
amount =float(input("enter amount to withdrow: (multiple of 100):"))
available_amount=10000
available_note=100
counting=0
while counting<amount:
    if counting>available_amount:
        break
    counting =available_note
print(counting,"withdraw")
available_amount=available_amount-counting
print(available_amount)










    
