# while condition:
#     # body of while loop 
# else:
    # rest body statments 
#The else  block execut if the condion is false and the body of the while is executed when while condition is True
#if you terminate while loop by using break keyword else part is ignorde

# example
# count=1
# while count<=5:
#     print("inside the  loop ")
#     count=count+1
#     if count==3:
#         break
# else:
#     print('inside else')

# while loop with else
# count=1
# while count<3:
#     print("inside the loop")
#     count=count+1
# else:
#     print("inside the else block")


# while else with loop with else
count=1
while count<=3:
    print("inside loop")
    count=count+1
    if count ==2:
            break
else:
        print("inside else")
# nested while loop 
# while expression:
#        statment
#        statemtn2
#        statment3
#        while expression:
#               statment
        
i=1
while i<=3:
       print("out loop")
       j=1
       while j<=3:
             print("inner loop")
             j=j+1
else:
       print("inside the else block")

