lang1=["marathi",'kannada',"English",'hindi']
lang2=['frach','japana',"spanish"]
for lan in lang2:
    lang1.append(lang2)
print(lang1)

# extend()
lang3=lang1.extend(lang2)
print(lang3)
print("$"*24)
print(lang3)

# the uppend method exted list by appending  all the items from iterable iterable can be list, tuple 
# this method returns the iterable iterable can be list tuple set etc 

# This method does not returns anny value rather thatn modifies the list items  it returns none

lan1=['marathi',"hindi","gujarathi",'urdhu']
lang2=['english',"frech","japani"]

lang1.extend(lang2)
print(lang1)