import math

n = int(input())
i = 0
while n > 0:
    i+=1
    if(math.sqrt(i) == int(math.sqrt(i))):
        print(i)
    n-=1
    