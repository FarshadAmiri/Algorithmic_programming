n, s = map(int, input().split())
wt = []
pack_len = []
for i in range(n):
    pack = list(map(int, input().split()))
    wt.append(pack[1:])
    pack_len.append(pack[0])

dp = [[None for i in range(s+1)] for j in range(n+1)]
par = [[None for iii in range(s+1)] for jjj in range(n+1)]


def knapsack(s, wt, n, pack_len):
    global dp
    global par
    for i in range(0,n+1):
        for j in range(0,s+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                par[i][j] = (0,0)
            elif min(wt[i-1]) <= j:
                dp2 = []
                dp2.append(dp[i - 1][j - min(wt[i - 1])] + 1)
                summ = sum(wt[i-1])
                if summ <= j:
                    dp2.append(dp[i-1][j-sum(wt[i-1])]+pack_len[i-1]) #All
                else:
                    dp2.append(-1e20)
                dp2.append(dp[i-1][j]) #Nothing
                m = max(dp2)
                dp[i][j] = m
                ind = dp2.index(m)
                if ind == 0:
                    par[i][j] = (1, min(wt[i-1]))
                elif ind == 1:
                    par[i][j] = (2, summ)
                else:
                    par[i][j] = (0, 0)
            else:
                dp[i][j] = dp[i-1][j]
                par[i][j] = (0, 0)
    return dp[n][s]


knapsack(s, wt, n, pack_len)
print(dp[n][s])

code = ''
CurrentRemainingWeight = s
for i in reversed(range(1,n+1)):
    if par[i][CurrentRemainingWeight] == None:
        pass
    elif par[i][CurrentRemainingWeight][0] == 1:
        code = code + '1'
        CurrentRemainingWeight -= par[i][CurrentRemainingWeight][1]
    elif par[i][CurrentRemainingWeight][0] == 2:
        code = code + '2'
        CurrentRemainingWeight -= par[i][CurrentRemainingWeight][1]
    elif par[i][CurrentRemainingWeight][0] == 0:
        code = code + '0'

print(code[::-1])