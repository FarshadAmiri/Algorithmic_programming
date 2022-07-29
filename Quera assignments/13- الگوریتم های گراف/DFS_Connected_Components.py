import sys
sys.setrecursionlimit(10**5 + 100)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(m)]

adj = [[] for i in range(n+1)]
mark = [False] * (n + 1)
components = list()
connected_components = list()

for i,j in graph:
    adj[i].append(j)
    adj[j].append(i)


def DFS(v):
    mark[v] = True
    components.append(v)
    for u in adj[v]:
        if not mark[u]:
            DFS(u)


for i in range(1, n + 1):
    if mark[i]:
        continue
    DFS(i)
    connected_components.append(components)
    components = []

print(connected_components)