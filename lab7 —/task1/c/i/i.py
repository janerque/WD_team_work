n = int(input())
cnt = 0
i = 1
j = 1
while i*i <= n:
    if n % i == 0:
        cnt += 1
    i += 1

while j*j < n:
    if n % j == 0:
        cnt += 1

    j += 1

print(cnt)