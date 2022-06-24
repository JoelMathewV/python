a=10
b=20
def c():
    global b
    a=45
    b=56
c()
print(a)
print(b)
