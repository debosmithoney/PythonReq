n = int(input())
p = list(map(int, input().strip().split()))
p = [0]+p
c = 0
for i in range(1, n):
    if (p[i] == i):
        p[i], p[i + 1] = p[i + 1], p[i]
        c += 1
if (p[n] == n):
    p[n - 1], p[n] = p[n], p[n - 1]
    c += 1
print(c)