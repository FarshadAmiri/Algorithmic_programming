n = int(input())
q = []
for i in range(n):
    q.append(int(input()))

d = {1:1, 2:1, 3:2, 4:3}

for i in range(5,10**5+1):
    d[i] = int((d[i - 1] + d[i - 2] + d[i - 3] - d[i - 4]) % (1e9+7))

for i in q:
    print(d[i])