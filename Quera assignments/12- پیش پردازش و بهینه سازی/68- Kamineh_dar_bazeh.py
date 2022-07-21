import math
# n, q = map(int, input().split())
# s = input().split()
# s = [int(i) for i in s]
# queries = [input().split() for i in range(q)]
# queries = [(int(i), int(j)) for i,j in queries]
n, q, s, queries = 7,3, [2, 1, 5, 4, 10, 2, 0], [(0, 6), (2, 4), (4, 4)]

print(s)
print(queries)

print(math.log)

rmq = [[None for j in range(len(s))] for i in range(int(math.log(len(s), 2))+1)]
def preprocess_rmq(array):
    global rmq
    for i in range(len(array)):
        rmq[0][i] = array[i]
    for k in range(1, int(math.log(len(array),2)) + 1 ):
        for i in range(len(array)):
            if (i + (2 ** (k - 1))) < len(array):
                rmq[k][i] = min(rmq[k - 1][i], rmq[k - 1][i+(2**(k-1))])
            else:
                rmq[k][i] = rmq[k - 1][i]

preprocess_rmq(s)
print(rmq)

def rmqMin(l,r):
    global s, rmq
    ans = 1e7
    for t in range(int(math.log(len(s), 2)),-1, -1):
        if (2 ** t) <= r - l:
            ans = min(ans, rmq[t][l])
            l += (2 ** t)
    return ans

for l,r in queries:
    print(rmqMin(l,r))
