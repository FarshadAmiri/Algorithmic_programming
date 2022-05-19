def puzzle(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j], end=" ")
        print()

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def Suduko(grid, row, col):
    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, 10 , 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


sdk = []
for row in range(9):
   sdk.append(list(map(int, input().split())))


if (Suduko(sdk, 0, 0)):
    puzzle(sdk)
else:
    print("No solution exists")