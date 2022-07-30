import sys
sys.setrecursionlimit(10**5 + 100)

n = int(input())
vertices = [tuple(map(int, input().split())) for i in range(n-1)]
q = int(input())
friends = [int(input()) for i in range(q)]

# print(vertices, friends, sep='\n')

# ---------------------------------------------------------
adj = list()
for i in range(n+1):
    adj.append(list())

distance = [10**9] * (n + 1)
queue = list()
prev = [None] * (n + 1)

for u,v in vertices:
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


BFS(1)

ans = None
dist = 10**30
for i in friends:
    if distance[i] < dist:
        dist = distance[i]
        ans = i
    elif distance[i] == dist:
        if ans != None:
            if i < ans:
                ans = i
        elif ans == None:
            ans = i

print(ans)