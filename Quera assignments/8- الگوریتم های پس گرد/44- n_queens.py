n, k = map(int, input().split())

# Generating Board Cells
board = dict()
for i in range(n):
    for j in range(n):
        board[(i, j)] = None

# Queens coordination list
queens = []

def invalid_cells(board, queens):
    for q in queens:
        q_x = q[0]
        q_y = q[1]
        for i in range(n):
            board[(q_x, i)] = 'invalid'
            board[(i, q_y)] = 'invalid'
        board[(q_x, q_y)] = 'Q'



ans = 0
def Queen_appointing(n,k):
    global ans
    global board

    n_q = list(board.values()).count('Q')
    if n_q < k:
        Queen_appointing(n, k-n_q)
    else:
        ans+=1

    for cell in board:
        if board[cell] == None:
            board[cell] = 'Q'
            n_q = list(board.values()).count('Q')
            Queen_appointing(n, k - n_q)






if k > n:
    print(0)
else:
    Queen_appointing(n, k)