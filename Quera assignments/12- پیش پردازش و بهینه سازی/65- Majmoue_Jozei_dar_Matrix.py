n, q = map(int, input().split())
mtx = [input().split()  for i in range (n)]
queries = [input().split() for i in range(q)]
mtx = [[int(j) for j in i] for i in mtx]
queries = [[int(j) for j in i] for i in queries]

# print(mtx)

ps = [[None for j in range(n+1)] for i in range(n+1)]

for i in range(n + 1):
    ps[0][i] = 0
    ps[i][0] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        ps[i][j] = mtx[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

# print(ps)

for i in queries:
    x,y,X,Y = i[0], i[1], i[2], i[3]
    print(ps[X+1][Y+1] - ps[X+1][y] - ps[x][Y+1] + ps[x][y])