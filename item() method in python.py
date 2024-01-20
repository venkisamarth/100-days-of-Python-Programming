# in python dictionary,items() mehtod is used to return list with all dictionary keys with values
# syntax.items() 
# no parameters are allowed 

fees ={"karan":12000,"jeson":3000,"john":14000}
print("dictionary items are")
fees_view=fees.items()
print(fees_view)
print(type(fees_view))

print("*"*100)
fees_view=list(fees.items())
for ele in fees_view:
    print(ele)

fees={}
print("dictionary items are :")
fees_view =list(fees.items())
print(fees_view)




