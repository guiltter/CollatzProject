

def collatz(x):
 y=0
 while True:
     y+=1
     if x == 0 or x ==1:
         return None
     elif x%2 == 0:
         x = x/2
     else:
         x = x*3+1
     if x == 1:
         break
 print ("The number amounted to:",x)
 print("The number of steps taken to get there was:",y)
 return (x,y)
collatz(30)