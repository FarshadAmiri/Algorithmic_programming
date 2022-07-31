import time
x = []
for row in range(9):
   x.append(list(map(int, input().split())))

sdk=[]
for j in range(9):
   sdk.append([x[i][j] for i in range(9)])

# print(sdk)
def sudoku_checker(sudoku, cell_coord):
   def checker(array, cell):
      for i in array:
         if i == cell:
            return False

   nx, ny = cell_coord[0], cell_coord[1]

   # check columns
   col = sudoku[nx].copy()
   col.remove(sudoku[nx][ny])
   if checker(col, sudoku[nx][ny]) == False:
       return False

   # check rows
   row = [sudoku[i][ny] for i in range(9)].copy()
   row.remove(sudoku[nx][ny])


   if checker(row, sudoku[nx][ny]) == False:
       return False

   #check squares
   sq_x = [i for i in range((nx//3)*3,(((nx//3)+1)*3))]
   sq_y = [i for i in range((ny//3)*3,(((ny//3)+1)*3))]

   square = [[sudoku[i][j] for j in sq_y] for i in sq_x]
   square = [item for sublist in square for item in sublist]

   square.remove(sudoku[nx][ny])
   if checker(square, sudoku[nx][ny]) == False:
       return False

   return True


def print_answer(sudoku):
      ans = []
      for j in range(9):
         ans.append([sudoku[i][j] for i in range(9)])
      for i in ans:
         for j in i:
            print(j, end=' ')
         print()
c = 0
pp = 0
def find_solution(sudoku):
   global pp, c
   sudoku_flatten = [item for sublist in sudoku for item in sublist]
   sudoku_solved = None
   if sudoku_flatten.count(0) == 0:
       for i in range(9):
           for j in range(9):
                if sudoku_checker(sudoku, (i,j)) == False:
                    sudoku_solved = False
       if sudoku_solved == None:
           print_answer(sudoku)
           pp = 1
           return True

   zeros = []
   for i in range(9):
      for j in range(9):
         if sudoku[i][j] == 0:
            zeros.append((i,j))
   if len(zeros) == 0:
      return

   for n in range(1,10):
      nx = zeros[0][0]
      ny = zeros[0][1]
      sudoku[nx][ny] = n
      c += 1
      if sudoku_checker(sudoku, (nx, ny)) == True:
          if find_solution(sudoku):
              return True
   sudoku[nx][ny] = 0
   return pp

t1 = time.time()
answer = find_solution(sdk)
print(f'Duration: {(time.time() - t1):.5f} seconds')
print(f'{c} number assigning')
if answer == 0:
    print('No solution exists')