num=int(input("enter a number"))
while True:
    for i  in range(1,11):
        print(f"{num}*{i}={num*i}")
    ans=input("Do you want to contniue(y/n)")
    ans=ans.lower()
    if ans!="y":
        break

