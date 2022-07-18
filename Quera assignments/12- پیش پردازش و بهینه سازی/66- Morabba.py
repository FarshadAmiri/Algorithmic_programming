n, m, k = map(int, input().split())
mat = [input().split() for i in range(n)]
mat = [[int(j) for j in i] for i in mat]

queries = []
for x1 in range(n-k+1):
    for y1 in range(m-k+1):
        x2 = x1 + k - 1
        y2 = y1 + k - 1
        queries.append((x1,y1,x2,y2))


def matrix_arrays(matrix_boundary):
    x1, y1, x2, y2 = matrix_boundary[0], matrix_boundary[1], matrix_boundary[2], matrix_boundary[3]
    arrays = []
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arrays.append((i,j))
    return arrays


max_ones = -1
ans_matrices = []
for q1 in queries:
    queries2 = queries.copy()
    queries2.remove(q1)
    for q2 in queries2:
        union_arrays = set(matrix_arrays(q1)).union(set(matrix_arrays(q2)))
        sum = 0
        for i,j in union_arrays:
            sum += mat[i][j]
        if sum > max_ones:
            max_ones = sum
            ans_matrices = [q1, q2]

union_arrays = set(matrix_arrays(ans_matrices[0])).union(set(matrix_arrays(ans_matrices[1])))
for i,j in union_arrays:
    mat[i][j] = 0

ans = 0
for i in mat:
    for j in i:
        ans += j

print((m*n) - ans)