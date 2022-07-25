n, k = map(int, input().split())
s = list(map(int, input().split()))
b = [None] * n

for i in range(n):
    b[i] = s[i] - (i * k)
b.sort()

if n % 2 == 1:
    m = b[int((n+1)/2) - 1]
else:
    m = b[int(n/2) - 1]

ans = 0
for i in range(n):
    ans += abs(m - b[i])
print(ans)