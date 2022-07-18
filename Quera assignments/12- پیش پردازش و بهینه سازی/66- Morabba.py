n, m, k = map(int, input().split())
matrix = [input().split() for i in range(n)]
matrix = [[int(j) for j in i] for i in matrix]

# matrix = [[1, 1, 0], [1, 1, 0], [0, 1, 0]]
# matrix = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1]]
# matrix = [[0, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1]]

# --------------------------------------------------------------------------------------------------------
def matrix_partial_sums_dp(matrix):
    n = len(matrix)
    ps = [[None for j in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        ps[0][i] = 0
        ps[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ps[i][j] = matrix[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
    return ps

def matrix_sum(ps, query):
    x, y, X, Y = query[0], query[1], query[2], query[3]
    return (ps[X + 1][Y + 1] - ps[X + 1][y] - ps[x][Y + 1] + ps[x][y])
# --------------------------------------------------------------------------------------------------------


for