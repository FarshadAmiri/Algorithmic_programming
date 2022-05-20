n, k = map(int, input().split())

def Knight_move(n, knight_loc):
    next_loc = []
    x = knight_loc[0]
    y = knight_loc[1]

    def move(n, loc, x_move, y_move, next_loc):
        x = loc[0]
        y = loc[1]
        if (x + x_move >= 0) and (x + x_move < n):
            if (y + y_move >= 0) and (y + y_move < n):
                next_loc.append((x + x_move, y + y_move))

    # Knight can move in 8 other cells at maximum
    move(n, knight_loc, -1, -2, next_loc) #1
    move(n, knight_loc, -2, +1, next_loc) #3
    move(n, knight_loc, -2, -1, next_loc) #2
    move(n, knight_loc, -1, +2, next_loc) #4
    move(n, knight_loc, +1, +2, next_loc) #5
    move(n, knight_loc, +2, +1, next_loc) #6
    move(n, knight_loc, +2, -1, next_loc) #7
    move(n, knight_loc, +1, -2, next_loc) #8

    return next_loc


