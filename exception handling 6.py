def get_square(): 
    try: 
        num=int(input("Enter the number:  "))
        print("square of the number is:",num**2)
    except Exception as e : 
        print(e)
        get_square()
get_square()
print("rest of code")

# a pinfull i exceptio handling 
try : 
    f=open("data1.txt","r")
    my_data=f.read()
    print(my_data)
except Exception as e: 
    print(e)
else: 
    print("read operation success")
finally: 
      try:
          f.close()
      except: 
          pass
