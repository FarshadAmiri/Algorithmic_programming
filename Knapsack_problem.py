# wt = list(map(int,input().split())) #Objects' Weights
wt = [8, 5, 6, 7, 3, 6, 8, 2, 8, 4]
# v = list(map(int,input().split())) #Objects' values
val = [18, 9, 17, 16, 6, 10, 10, 4, 19, 3]
# s = int(input()) #Maximum weight capacity
s = 40

assert len(wt) == len(val), 'w and v do not have same lenghts!'
n = len(wt)
dp = [[None for i in range(s+1)] for j in range(n+1)]
par = [[None for iii in range(s+1)] for jjj in range(n+1)]

def knapsack(s, wt, val, n):
    global dp
    global par
    for i in range(0,n+1):
        for j in range(0,s+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i-1]] + val[i-1])
                if dp[i-1][j] > dp[i-1][j-wt[i-1]] + val[i-1]:
                    par[i][j] = 0
                else:
                    par[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]
                par[i][j] = 0
    return dp[n][s]


knapsack(s, wt, val, n)
print(dp[n][s])

CurrentRemainingWeight = s
for i in reversed(range(n+1)):
    if par[i][CurrentRemainingWeight] == 1:
        print(f"{i}'th object has been taken")
        CurrentRemainingWeight -= wt[i-1]