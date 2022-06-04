# Three out of 5 tests went time limit exceeded!
t = int(input())
series = []

for i in range(t):
    _ , k = map(int, input().split())
    series.append((list(map(int ,input().split())), k))

def solve(serie, k):
    ps = [0]
    for i in range(len(serie)):
        ps.append(ps[-1] + serie[i])
    ps = sorted(ps)
    print(ps)
    ans = 0
    for id, i in enumerate(ps):
        for j in ps[id+1:]:
            if abs(i-j) > k:
                ans += 1
    return ans

for serie, k in series:
    print(solve(serie, k))
