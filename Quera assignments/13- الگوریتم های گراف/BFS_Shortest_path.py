import sys
sys.setrecursionlimit(10**5 + 100)

n, m = map(int, input().split())  #Number of Edges and vertices respectively
s, e = map(int, input().split())  #Start and end edge

adj = list()
for i in range(n+1):
    adj.append(list())

distance = [10**9] * (n + 1)
queue = list()
prev = [None] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def BFS(root):
    distance[root] = 0
    queue.append(root)
    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if distance[u] > distance[v] + 1:
                distance[u] = distance[v] + 1
                prev[u] = v
                queue.append(u)


BFS(s)

dist = distance[e]
dist = dist if dist != 1000000000 else -1
print(dist)  #Shortest path length (from 's' to 't')

if dist != -1:
    path = []
    path.append(e)
    while e != s:
        path.append(prev[e])
        e = prev[e]
    print(*path[::-1])