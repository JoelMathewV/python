import random
print('welcom to the lucky game')
print('here you rill have 10 chances to choose the number which the computer has decided')
x=random.randint(0,30)
c=0
while c<10:
      y= int(input('enter a number between 0 - 30:'))
      if y==x:
          print("you are the winner")
          break
      else:
          c+=1
      if not c<10:
          print('you are the loser, try again later')

