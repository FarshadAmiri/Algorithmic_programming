m,n = map(int, input().split())
a = []

for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

# print(a)

b = dict()
for i in range(n):
    for j in range(m):
        for k in range(-1,m):
            b[(i,j,k)] = 0

for i in range(n):
    for j in range(m):
        b[(i, j, j)] = a[j][i]
        for k in range(j,m):
            b[(i,j,k)] = b[(i,j, k-1)] + a[k][i]


answer = 10e-50

for r1 in range(m):
    for r2 in range(r1,m):
        max_sum = dict()
        max_sum[0] = b[(0,r1,r2)]
        for c2 in range(1,n):
            max_sum[c2] = max(b[(c2,r1,r2)], max_sum[c2-1] + b[(c2,r1,r2)])
        answer = max(max(max_sum.values()), answer)

print(int(answer))