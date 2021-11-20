n = int(input())
h = list(map(int, input().split()))

h_uniques = sorted(set(h))
h = [h_uniques.index(i)+1 for i in h]

dp = [[0 for r in range(n)] for l in range(n)]
for i in range(n):
    dp[i][i] = 1

ans = 0
for length in range(0,n):
    for l in range(n - length):
        r = l + length
        dp[l][r] = dp[l][r-1]
        if h[l] == h[r]:
            dp[l][r] += 1
            for x in range(l+1, r):
                if h[x] >= h[l]:
                    dp[l][r] += dp[x][r - 1]
    ans = (ans%(1e9+7) + dp[n - length - 1][n - 1] % (1e9+7)) % (1e9+7)

print(int(ans%(1e9+7)))