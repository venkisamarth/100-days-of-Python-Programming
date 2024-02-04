class A: 
    pass
class B: 
    pass 
class C: 
    pass 
class x(A,B,C): 
    pass
class Y(B,C): 
    pass 
class p(x,Y):
    pass 
print(p.mro())