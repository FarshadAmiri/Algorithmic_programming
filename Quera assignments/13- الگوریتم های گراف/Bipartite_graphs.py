# https://quera.org/college/3016/chapter/8244/lesson/27793/?comments_page=1&comments_filter=ALL
#To distingiuish whether a graph is Bipartite or not
# Based on DFS
import sys
sys.setrecursionlimit(10**5 + 100)

n, m = map(int, input().split())
adj = list()
for i in range(n+1):
    adj.append(list())
mark = (n+1)*[False]
color = (n+1)*[0]
bipartite = True;
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def DFS(v, parent):
    mark[v] = True
    if parent != -1:
        color[v] = 1 - color[parent]
    else:
        color[v] = 1
    for u in adj[v]:
        if not mark[u]:
            DFS(u, v)
        elif color[u] == color[v]:
            global bipartite
            bipartite = False

for i in range(1, n+1):
    if mark[i]:
        continue
    DFS(i, -1) #root does not have parent.

if bipartite:
    print("Graph Is Bipartite")
else:
    print("Graph Is Not Bipartite")