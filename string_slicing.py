# To access a range of items(substring) we will use slicing 
 
# you can return range character using slicing  

# [:] is a slice operator 

# systax 
# var_name[start:stop:step]
# start starting point of the substring 
# stop  It is the ending point of the substring 
# step diffrence between indexing 

name="code yug"
print(name[0:3:1])
print(name[2:4])
print(name[0:5:2])
print(name[:4])
print(name[::])

print(name[0::3])
print(name[-1:-4:1])

print(name[-1:-5:-2])
print(name[-1:-5:-2])
print(name[-2:-6:2])

print(name[-3:-11])
print(name[-1:-11:-1])
print(name[2:6:1])
