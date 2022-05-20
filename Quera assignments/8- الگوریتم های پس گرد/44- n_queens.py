n, k = map(int, input().split())
ans = 0
queens = []   #First indice is the column number and second indice is the row number

def kqueens(n, k, col):
    global ans, queens
    if col == n :
        if k == 0:
            ans += 1
        return
    if k > 0:
        for row in range(n):
            if row in [i[1] for i in queens]:
                continue
            if (col + row) in [(i + j) for i, j in queens]:
                continue
            if (col - row) in [(i - j) for i, j in queens]:
                continue
            queens.append((col, row))
            kqueens (n, k - 1, col + 1)
            queens.remove((col, row))
    kqueens(n, k, col + 1)


kqueens(n, k, 0)
print(ans)