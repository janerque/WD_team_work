s=input()
arr=list(map(int,(input()).split()))
n=len(arr)
c=0
for i in range(1,n-1):
    if (arr[i] > arr[i-1]) & (arr[i] > arr[i+1]):
        c+=1
print(c)