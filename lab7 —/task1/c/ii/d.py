n = int(input())
i = 1
while i < n:
   i = i * 2
if i == n:
   print("YES")
else:
   print("NO")

n = int(input())
# k = int(input())
t = 0
k = 2

while n > k**t:
    t += 1
else:
    if n == k**t:
        print("YES")
    else:
        print("NO") 