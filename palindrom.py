def is_palindrom(x):
    x=str(x)
    left,right=0,len(x)-1
    if x[left]!=x[right]:
        return False
    while left<right:
        left+=1
        right-=1
print(is_palindrom(121))
print(is_palindrom(-121))