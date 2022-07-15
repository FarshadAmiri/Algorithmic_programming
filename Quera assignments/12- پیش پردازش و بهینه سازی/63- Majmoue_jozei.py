_ , q = map(int, input().split())
serie = list(map(int, input().split()))
queries = [tuple(map(int,input().split())) for k in range(q)]

# print(serie)
# print(queries)

ps = [0]
for i in serie:
    ps.append(i+ps[-1])

# print(ps)

for l,r in queries:
    if l == r:
        print(serie[l])
    else:
        print(ps[r + 1] - ps[l])