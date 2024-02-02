def case1():
    print( "This is case 1")

def case2():
    print ("This is case 2")

def case3():
    print ("This is case 3")

def default_case():
    print ("This is the default case")

def switch_case(argument):
    switcher = {
        1: case1,
        2: case2,
        3: case3
    }
    # Get the function corresponding to the argument
    func = switcher.get(argument, default_case)
    # Execute the function
    func()

# Example usage:
switch_case(2)  # Output: This is case 2
switch_case(4)  # Output: This is the default case

def case1():
    print ("This is case 1")

def case2():
    print ("This is case 2")

def case3():
    print ("This is case 3")

def default_case():
    print ("This is the default case")

def switch_case(argument):
    switcher = {
        1: case1,
        2: case2,
        3: case3
    }
    # Get the function corresponding to the argument
    func = switcher.get(argument, default_case)
    # Execute the function
    func()

# Example usage:
switch_case(2)  # Output: This is case 2
switch_case(4)  # Output: This is the default case
# by using if elif else: 
marks=float(input("enter marks"))
if marks>=80 and marks<=18: 
    print("you can got grade A")
elif marks <80 and  marks>=60: 
    print("you got grade B")
elif marks<60 and marks>=35: 
    print("you got grade c")
else: 
    print("you are falid /incorected marks")
    