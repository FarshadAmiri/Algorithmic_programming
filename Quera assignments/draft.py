x = []
for row in range(9):
   x.append(list(map(int, input().split())))

sudoku=[]
for j in range(9):
   sudoku.append([x[i][j] for i in range(9)])

print(sudoku)

sudoku_flatten = [item for sublist in sudoku for item in sublist]
print(sudoku_flatten)