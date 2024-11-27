print("Importing my_module....")
test="Test String"
def  find_index(to_serch,target):
    ''' find the index of a value in a sequance'''
    for i ,value in enumerate(to_serch):
        if value ==target:
            return i 
    return -1

