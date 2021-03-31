n = input()
sum = 0
cnt = 0
for i in range(len(n) - 1, -1, -1):
    sum += int(n[i])*(2**(cnt))
    cnt += 1
print(sum)