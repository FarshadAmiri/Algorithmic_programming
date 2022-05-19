n, k = map(int, input().split())
ans = 0
queens = [] #First indice is the column number and the second one is the row number

def kqueens(n, k, col):
    global ans, queens
    if col == n-1:
        if k == 0:
            ans += 1
        return
    if k>0:
        for row in range(n):
            if row in [i[1] for i in queens]:
                continue
            if (row + col) in [(i + j) for i, j in queens]:
                continue
            if (row - col) in [(i - j) for i, j in queens]:
                continue
            queens.append((row, col))
            kqueens (n, k - 1, col + 1)
            queens.remove((row, col))
        kqueens(n, k, col + 1)


kqueens(n, k, 0)
print(ans)