import math
n , q = map(int, input().split())
series = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(q)]


list = []
par = [0] * (n + 1)
for i in range(n):
    par[i+1] += par[i] + series[i]


def getsum(l,r):
    global par
    result = par[r+1] - par[l]
    for (idx, x) in list:
        if idx >= l and idx <= r:
            result += x
    print(result)


def change_val(idx, new_val):
    global list, series
    list.append((idx, new_val - series[idx]))
    series[idx] = new_val


def update_partial_sum():
    global list, par
    for i in range(n):
        par[i + 1] = par[i] + series[i]
    list = []


counter = 0
for query_type, i,j in queries:
    if counter == int(math.sqrt(n)):
        update_partial_sum()
        counter = 0
    if query_type == 1:
        getsum(i, j)
    if query_type == 2:
        change_val(i, j)
        counter += 1