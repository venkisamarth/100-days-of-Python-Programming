# get() method
employee={"name":"raj",'age':23,"salary":5000}
print(employee["name"])
# This method returns the value of the specified value of key
# if key  found defalult value is printed

# syntax= dict_name.get(key,default_value)
# print("101 statments ")

# print(employee["na"])
print(employee.get("salary"))
print(employee.get("sal",'not found'))