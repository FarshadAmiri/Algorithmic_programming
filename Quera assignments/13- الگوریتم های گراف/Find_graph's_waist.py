# https://quera.org/college/3016/chapter/8244/lesson/27794/?comments_page=1&comments_filter=ALL
# This code works for simple graphs.
# Based on BFS Tree
# Waist = minimum cycle (cycle with the minimum length in the graph)

n, m = map(int, input().split())
adj = list()
for i in range(n+10):
    adj.append(list())
distance = (n+10)*[10**9]

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def BFS(root, deleted):
    distance = (n+10)*[10**9]
    distance[root] = 0
    queue = list()
    queue.append(root)
    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if v == root and u == deleted:
                continue #ignore deleted edge
            if distance[u] > distance[v] + 1:
                distance[u] = distance[v] + 1
                queue.append(u)

length = 10**9
for i in range(1, n+1):
    for u in adj[i]:
        BFS(i, u)
        length = min(length, distance[u] + 1)

if length == 10**9:
    print("Graph Does Not Have Cycle")
else:
    print("Minimum Cycle Length is :", length)