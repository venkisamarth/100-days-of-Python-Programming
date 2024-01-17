# dictionary nutable
#we can modify value using follwoing systax 
#dict_name=[key]=new_value

fees={"sachi":2000,"virat":23232,"sourave":3223}
print(fees)
print(id(fees))
fees["virat"]=2324343
print(id(fees))
print(fees)

fees["shantanu"]=34434
print(fees)



fees["virat"]=fees["virat"]-1000
print(fees)


