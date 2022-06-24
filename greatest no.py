a=int(input('enter the 1st no.:'))
b=int(input('enter the 2nd no.:'))
c=int(input('enter the 3rd no.:'))
print('the ascending order of no is-')
if a>b and a>c:
    if b>c :
        print(c,b,a)
    else:
        print(b,c,a)
elif b>a and b>c:
    if a>c :
        print(c,a,b)
    else:
        print(a,c,b)
else:
    if c>a and c>b:
        
        if a>b :
            print(b,a,c)
        else:
            print(a,b,c)
