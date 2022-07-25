n = int(input())
s = list(map(int, input().split()))

s.sort()

if n % 2 == 1:
    m = s[int((n+1)/2) - 1]
else:
    m = s[int(n/2) - 1]

ans = 0
for i in range(n):
    ans += abs(m - s[i])

print(m, ans, sep=' ')