n, q = map(int, input().split())

v = [[i+1] for i in range(n)]

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        v[query[2] - 1] = list(set(v[query[2] - 1]).union(v[query[1] - 1]))
        v[query[1] - 1] = []
    elif query[0] == 2:
        print(len(v[query[1] - 1]))
    else:
        ans = sorted(v[query[1] - 1])
        if len(ans) == 0:
            print(-1)
        else:
            print(*ans)
