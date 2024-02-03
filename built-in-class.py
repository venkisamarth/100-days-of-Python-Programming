# getattr(object_name,attribute_name)
# setattr(obje_name,attribute_name,new_attribute)
# delattr(obje_name,attribute_name)
# hasattr(object_name,attriute)
class Employee: 
  def __init__(self,nm,ag): 
    self.name=nm
    self.age=ag

e1=Employee("raj",23)
e2=Employee("venki",23)
print(getattr(e1,"name"))
print(getattr(e2,"name"))

print(hasattr(e2,"name"))
print(hasattr(e2,"name"))

delattr(e1,"name")
e1.name="veki"
print(getattr(e1,"name"))
setattr(e1,"name","venkisamarth")
print(e1.name)
