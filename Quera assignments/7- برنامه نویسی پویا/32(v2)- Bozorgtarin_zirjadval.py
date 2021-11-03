m,n = map(int, input().split())
a = []

for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

# print(a)

b = dict()
for i in range(n):
    for j in range(m):
        for k in range(m):
            b[(i,j,k)] = 0

for i in range(n):
    for j in range(m):
        b[(i, j, j)] = a[j][i]
        for k in range(j+1,m):
            b[(i,j,k)] = b[(i,j, k-1)] + a[k][i]


max_sum = dict()

for r1 in range(m):
    for r2 in range(r1,m):
        max_sum[0,r1,r2] = b[0,r1,r2]
        for c2 in range(1,n):
            max_sum[c2,r1,r2] = max(b[c2,r1,r2], max_sum[c2-1,r1,r2] + b[c2,r1,r2])


print(int(max(max_sum.values())))