a = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, a):
    if arr[i] > arr[i - 1]:
        cnt += 1
print(cnt)