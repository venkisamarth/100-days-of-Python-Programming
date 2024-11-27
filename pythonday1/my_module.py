print("Imported my module...")
test ="Test string"
def find_index(to_search, target):
    ''' find the index of a value in a sequance '''
    for i, value  in enumerate(to_search):
        if value ==target:
            return i 
    return -1
# when we import the module it check the multiple locations 
