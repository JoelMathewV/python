a=int(input("enter a no"))
num = 2
while num <= a:
    div = 2
    while div < num:
        if num % div==0:
            num=num+1
        else:
            div=div+1
    print(num)
    num=num+1
