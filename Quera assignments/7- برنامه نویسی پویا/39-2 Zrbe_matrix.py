n = int(input())
a = list(map(int, input().split()))

dp = [[None for ii in range(n)]for jj in range(n)]
dp[0][1] = a[0]*a[1]*a[2]

for i in range(n):
    dp[i][i] = 0

def dp_m(l,r):
    global dp
    if dp[l][r] != None:
        return dp[l][r]
    res = 1e100
    for i in range(l,r):
        res = min(res, dp_m[l][i] + dp_m[i+1][r] + a[l]*a[i+1]*a[r+1])
    dp[l][r] = res
    return dp[l][r]

print(dp[0][n-1])
print(dp)