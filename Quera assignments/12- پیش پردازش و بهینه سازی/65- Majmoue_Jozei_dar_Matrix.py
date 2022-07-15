n, q = map(int, input().split())
mtx = [input().split()  for i in range (n)]
queries = [input().split() for i in range(q)]
mtx = [[int(j) for j in i] for i in mtx]
queries = [[int(j) for j in i] for i in queries]

print(mtx)
print(queries)