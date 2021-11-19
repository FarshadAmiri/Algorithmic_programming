s = input()
p = input()

dp = [[0 for jj in range(len(p)+1)] for ii in range(len(s)+1)]
seq = [['' for jjj in range(len(p)+1)] for iii in range(len(s)+1)]

for i in range(len(s)+1):
    for j in range(len(p)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif s[i-1] == p[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            seq[i][j] = seq[i-1][j-1] + s[i-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            seq[i][j] = max(seq[i][j - 1], seq[i - 1][j], key = len)

# print(dp)
# print(seq)
print(dp[len(s)][len(p)])
print(seq[len(s)][len(p)])