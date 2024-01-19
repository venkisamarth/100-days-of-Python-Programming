# view objects of Dictionary 
# there viws we can create 
# 1 view of key -value pairs :-using items() method
# 2 view of keys :- using  keys() method
# 3 view of values :- using values() method 

fees =  {'karan':12000,"jeson":13000,"john":14000}
fees_list=list(fees.values())
print(fees_list)
print(type(fees_list))
total_collection =sum(fees_list)
print("total amount to collect:",total_collection)
sum=0
for item in fees.items():
    print(item)


my_cart={"mobile":14000,'earphone':1500,"watch":4000,'laptop':600000}
prices=list(fees.values())
print(prices)
sum=0
for ele in prices:
    sum=sum+ele
print(sum)

print(sum(prices))



