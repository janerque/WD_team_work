a = int(input())

arr = list(map(int, input().split()))
exist = False
for i in range(1, a):
    if arr[i] > 0 and arr[i - 1] > 0:
        exist = True
    elif arr[i] < 0 and arr[i - 1] < 0:
        exist = True
    
if exist == True:
    print("YES")
else:
    print("NO")