m,n = map(int, input().split())
a = [[0 for i in range(n)] for j in range(m)]

c = 0
for i in range(m):
    row = list(map(int, input().split()))
    for count, value in enumerate(row):
        a[c][count] = value
    c += 1

a = list(reversed(a))
dp_dict = [[None for i in range(n)] for j in range(m)]

dp_dict[0][0] = a[0][0]

def dp(i,j):
    if dp_dict[i][j] != None:
        return dp_dict[i][j]
    elif i==0:
        res = dp(i,j-1) + a[i][j]
        dp_dict[i][j] = res
    elif j==0:
        res = dp(i-1, j) + a[i][j]
        dp_dict[i][j] = res
    else:
        res =  max(dp(i, j-1) + a[i][j], dp(i-1, j) + a[i][j])
        try:
            dp_dict[i][j] = res
        except:
            pass
    return res

dp(m-1, n-1)
print(dp_dict[m-1][n-1])

i,j = m-1, n-1
path = ''
while (i + j > 0):
    if (i > 0) and (j > 0):
        if dp_dict[i][j-1] >= dp_dict[i-1][j]:
            path = path + 'R'
            j -= 1
        elif dp_dict[i][j-1] < dp_dict[i-1][j]:
            path = path + 'U'
            i -= 1
    elif (i == 0) and (j > 0):
        path = path + 'R'
        j -= 1
    elif (j == 0) and (i > 0):
        path = path + 'U'
        i -= 1

path = path[::-1]
print(path)
