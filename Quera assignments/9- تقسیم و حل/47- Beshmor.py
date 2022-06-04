t = int(input())
series = []

for i in range(t):
    _ , k = map(int, input().split())
    series.append((list(map(int ,input().split())), k))

# print(series)

def solve(serie, k):
    ps = [(0, serie[0])]
    for i in range(len(serie)-1):
        ps.append((i + 1 , ps[-1][1] + serie[i + 1]))
    # return ps
    sorted_ps = sorted(ps, key = lambda x: x[1])
    return sorted_ps





for serie, k in series:
    print(solve(serie, k))
