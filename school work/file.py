# 5
f=open("hello.txt",'r')
a=f.readlines()
print(a)
f.close()


#6
fin=open("hello.txt","a+")
fout=open("world.txt","a+")
s=fin.readlines()
for j in s:
    if 'a' in j:
        fout.write(j)
 
b=fin.readlines()
c=fout.readlines()
print(b,c)
fin.close()
fout.close()
