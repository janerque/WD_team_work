import math

a = int(input())
n = int(input())
for i in range(a, n+1):
    if(int(math.sqrt(i)) == math.sqrt(i)):
        print(i, end = ' ')
        