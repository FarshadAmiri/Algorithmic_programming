q = int(input())
l = []
for i in range(q):
    a,b = map(int, input().split())
    l.append((a,b))

c = [[0 for i in range(2001)] for j in range(2001)]

for n in range(2001):
    for r in range(2001):
        if r==0 or r==n:
            c[n][r] = 1
        else:
            c[n][r] = (c[n-1][r] + c[n-1][r-1]) % (1e9+7)

for n,r in l:
    print(int(c[n][r]))