# https://quera.org/college/3016/chapter/8244/lesson/27791/?comments_page=1&comments_filter=ALL
# DFS Tree
import sys
sys.setrecursionlimit(10**5 + 100)

n, m = map(int, input().split())
adj = list()
for i in range(n+1):
    adj.append(list())
mark = (n+1)*[0]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
cycle_found = False

def DFS(v, parent):
    mark[v] = True
    for u in adj[v]:
        if not mark[u]:
            DFS(u, v) #u's parent is v.
        elif u != parent:
            global cycle_found
            cycle_found = True

for i in range(1, n+1):
    if mark[i]:
        continue
    DFS(i, -1) #root does not have parent.

    if cycle_found:
        print('Graph has Cycle.')
    else:
        print('Graph does not have Cycle.')