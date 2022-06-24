def alter(x,y=20):
    x=x*y
    y=x%y
    print(x,'*',y)
    return(x)
a=200
b=30
a=alter(a,b)
print(a,'$',b)
b=alter(b)
print(a,'$',b)
a=alter(a)
print(a,'$',b)
