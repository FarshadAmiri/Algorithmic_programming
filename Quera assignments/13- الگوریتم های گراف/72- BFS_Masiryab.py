import sys
sys.setrecursionlimit(10**5 + 100)

n, m = map(int, input().split())
s, e = map(int, input().split())
adj = list()
for i in range(n+1):
    adj.append(list())
distance = (n+1)*[10**9]
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
ans = distance[e]
ans = ans if ans != 1000000000 else -1
print(ans)


if ans != -1:
    path = []
    path.append(e)
    while e != s:
        path.append(prev[e])
        e = prev[e]
    print(*path[::-1])