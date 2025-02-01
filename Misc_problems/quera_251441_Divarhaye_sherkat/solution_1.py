# n_rows = int(input())

# colored_rows = []

# for i in range(n_rows):
#     l, r = map(int, input().split())
#     colored_rows.append((l, r))


import random, time
n_rows = 10000000
colored_rows = [(random.randint(1, 90), random.randint(2, 100)) for _ in range(n_rows)]

tic = time.time()

min_value = min(min(t) for t in colored_rows)
max_value = max(max(t) for t in colored_rows)

min_value , max_value
n_cols = max_value

mat = [[0] * n_cols for _ in range(n_rows)]



for row in range(n_rows):
    r, l = colored_rows[row]
    for i in range(r, l):
        mat[row][i] = 1


p = 0
for i in range(n_rows):
    for j in range(n_cols):
        if mat[i][j] == 1:
            c = 4
            if i > 0:
                if mat[i-1][j] == 1:
                    c -= 1

            if i < n_rows - 1:
                if mat[i+1][j] == 1:
                    c -= 1

            if j > 0:
                if mat[i][j - 1] == 1:
                    c -= 1

            if j < n_cols - 1:
                if mat[i][j + 1] == 1:
                    c -= 1

            p += c

print(p)

tac = time.time()
time_spent = tac - tic

print(f"{time_spent:.3} seconds took!")