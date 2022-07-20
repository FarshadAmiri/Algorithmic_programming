# n,k = map(int, input().split())
# requests = [input().split() for i in range(n)]
# requests = [(int(j),int(k)) for j,k in requests]
n , k = 3 , 2
requests = [(1, 3), (2, 3), (4, 4)]

max_b = max([j for i,j in requests])

dp = [0] * (max_b + 1)
dp[0] = 1

for i in range(1,max_b+1):
    dp[i] += dp[i-1]
    if i >= k:
        dp[i] += dp[i - k]

# print(dp)
ps = [0] * (max_b + 1)
ps[0] = dp[0]
for i in range(1,max_b+1):
    ps[i] = ps[i-1] + dp[i]

# print(ps)

for i,j in requests:
    print((ps[j] - ps[i-1]) % 1000000007)