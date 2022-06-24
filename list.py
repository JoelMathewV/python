a=eval(input('enter the first list'))
b=len(a)
for i in range(0,b):
    if a[i]>10:
       a[i]=10
print(a)
