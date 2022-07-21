n,k = map(int, input().split())
requests = [input().split() for i in range(n)]
requests = [(int(j),int(k)) for j,k in requests]

max_b = max([j for i,j in requests])

dp = [0] * (max_b + 1)
dp[0] = 1

for i in range(1,max_b+1):
    dp[i] += (dp[i-1]) % 1000000007
    if i >= k:
        dp[i] += (dp[i - k]) % 1000000007

ps = [0] * (max_b + 1)
ps[0] = dp[0]
for i in range(1,max_b+1):
    ps[i] = (ps[i-1] + dp[i]) % 1000000007

for i,j in requests:
    print((ps[j] - ps[i-1]) % 1000000007)