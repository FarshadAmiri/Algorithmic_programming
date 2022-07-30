from itertools import permutations
import math
n = int(input())
s = int(input().replace(' ',''))
n_fac = math.factorial(n)

perms = list(map(int, [''.join(p) for p in permutations(str(s))]))
# print(perms)


def transformable(w1, w2):
    w1, w2 = str(w1), str(w2)
    for x in range(1,n+1):
        w1_t = w1[:x][::-1] + w1[x:]
        w2_t = w2[:x][::-1] + w2[x:]
        if (w1 == w2_t) or (w1_t == w2):
            return True
    return False


two_diffs_vertices = set()
for i in range(n_fac):
    for j in range(n_fac):
        # if str_diff(fac[i], fac[j]) == True:
        #     two_diffs_vertices.append((fac[i], fac[j]))
        if transformable(perms[i], perms[j]) == True:
            two_diffs_vertices.add((min(i,j), max(i,j)))

# print(two_diffs_vertices)
# ---------------------------------------------------------------------
e_num = sorted(str(s))
for i in e_num:
    try:
        e_num = e_num + i
    except:
        e_num = '' + i
e_num = int(e_num)
e = perms.index(e_num)

adj = list()
for i in range(n_fac):
    adj.append(list())

distance = [10**30] * (n_fac)
queue = list()
prev = [None] * (n_fac)

for u,v in two_diffs_vertices:
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


BFS(perms.index(s))

dist = distance[e]
dist = dist if dist != 10**30 else -1
print(dist)