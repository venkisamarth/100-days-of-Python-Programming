# keeps a counter to iterable and returns it 
sports=["cricket","kabaddi",'tennis', 'badmiton']
enu_obj=enumerate(sports)
print(list(enu_obj))
print(type(enu_obj))

print(list(enu_obj))


for pos,ele in enumerate(sports):
    print(f"{pos}:{ele}")
print(list(enumerate(sports,1)))

import json
sports=['cricket',"kabbadi","tennis","badmiton"]
data=dict(list(enumerate(sports,1)))
open('data.json',"w+")
json.dump(data,'f')
f.close








