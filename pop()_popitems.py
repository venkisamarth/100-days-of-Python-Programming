# python pop method can be used to delete a key and value associated with it  

# syntax 

# dict_name.pop('key','value if key is not present')

lottery={"raju":101,"jay":104,"mahesh":110}
print("before deletion:",lottery)
deleted_value=lottery.pop("raju","not found")
print("after deletion of the element :",lottery)

# popitem method 
lottery={'raj':101,"jay":104,"mahesh":110}
print('before deletion :',lottery)
value=lottery.popitem()
print('after deltion:',lottery)
print(value)
print(lottery)
