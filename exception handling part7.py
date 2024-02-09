# write a program to that will sum the numbers in the given list 
def sum_of_int__list(my_list): 
    total=0 
    for ele in my_list: 
        try: 
            int(ele)
        except: 
            print(f'item {ele} is not a numbers')
        else: 
            total=total+ele
print(sum_of_int__list([1,2,3,"venki",2,3,4]))

# find the erro and fix it 
def total_likes(): 
    reviews=[{"image":3,"like":20,"count":20},
             {"image":6,"like":89,"count":23},
             {"image":7,"like":89,"count":23}]
    total=0 
    for reviews in reviews: 
        try: 
            total=reviews["like"]
        except: 
            pass 
    return total 
print(total_likes())