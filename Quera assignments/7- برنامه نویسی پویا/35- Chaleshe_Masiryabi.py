m,n = map(int, input().split())
a = [[0 for i in range(n)] for j in range(m)]

c = 0
for i in range(m):
    row = list(map(int, input().split()))
    for count, value in enumerate(row):
        a[c][count] = value
    c += 1

dp_table = [[[None, None] for i in range(n)] for j in range(m)]
dp_table[0][0][0], dp_table[0][0][1] = a[0][0], a[0][0]

for j in range(1,n):
    dp_table[0][j][0] = +1e50


def dp(i,j,k):
    if dp_table[i][j][k] != None:
        return dp_table[i][j][k]
    if k == 0:
        if j != n-1:
            if i != 0:
                res = min(dp(i-1, j, 0), dp(i-1, j, 1), dp(i, j + 1, 0)) + a[i][j]
        elif j == n-1:
            if i != 0:
                res = min(dp(i - 1, j, 0), dp(i - 1, j, 1)) + a[i][j]
    elif k == 1:
        if j != 0:
            if i != 0:
                res = min(dp(i-1, j, 0), dp(i-1, j, 1), dp(i, j - 1, 1)) + a[i][j]
            elif i == 0:
                res = min(dp(i, j - 1, 0), dp(i, j - 1, 1)) + a[i][j]
        elif j == 0 :
            if i != 0:
                res = min(dp(i - 1, j, 0), dp(i - 1, j, 1)) + a[i][j]
    dp_table[i][j][k] = res
    return res


for i in range(m):
    for j in range(n):
        dp(i,j,0)
        dp(i,j,1)

print(dp_table[m-1][n-1][1])