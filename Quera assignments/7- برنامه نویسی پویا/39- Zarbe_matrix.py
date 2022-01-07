n = int(input())
a = list(map(int, input().split()))

# m = [[None ,None] for iii in range(n)]
# m[0][0] = a[0]
# m[-1][1] = a[-1]
#
# for index, ai in enumerate(a[1:-1]):
#     m[index ][1] = ai
#     m[index+1][0] = ai
#
# print(m)

dp = [[None for ii in range(n-1)]for jj in range(n-1)]
# dp[0][0] = 0
dp[0][1] = a[0]*a[1]*a[2]
# dp[n-2][n-2] = 0
# dp[n-3][n-2] = a[n-2]*a[n-1]*a[n]

for i in range(n-1):
    dp[i][i] = 0

for i in range(n-1):
    for j in range(i,n-1):
        try:
            dp[i][j] = min(dp[i][j], dp[i][j] + dp[j][n-2] + a[i] * a[j+1] * a[n-2])
        except:
            continue


print(dp[0][n-2])
print(dp)