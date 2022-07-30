import sys
sys.setrecursionlimit(10**5 + 100)

n = int(input())
edges = [tuple(map(int, input().split())) for i in range(n)]
# n, edges = 4, [(1, 1), (3, 1), (3, 3), (1, 3)]
# n, edges = 4, [(1, 1), (2, 2), (3, 3), (3, 4)]

vertices  = set()
for i in range(n):
    e2_idx = [i for i in range(n)]
    e2_idx.remove(i)
    for j in e2_idx:
        e1 = edges[i]
        e2 = edges[j]
        if (e1[0] == e2[0]) or (e1[1] == e2[1]):
            vertices.add((min(i,j), max(i,j)))

# print(vertices)

adj = [[] for i in range(n)]
mark = [False] * (n)
components = list()
connected_components = list()

for i,j in vertices:
    adj[i].append(j)
    adj[j].append(i)


def DFS(v):
    mark[v] = True
    components.append(v)
    for u in adj[v]:
        if not mark[u]:
            DFS(u)


for i in range(n):
    if mark[i]:
        continue
    DFS(i)
    connected_components.append(components)
    components = []

print(len(connected_components) - 1)