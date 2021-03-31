n = int(input())
a = [int(i) for i in input().split()]
pos = 0
for i in a:
    if i%2 == 0:
        print(i, end=' ')