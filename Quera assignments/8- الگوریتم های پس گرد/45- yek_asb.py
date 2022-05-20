n, k = map(int, input().split())
final_possible_locs = set()
# It returns next possible knight locations based on its current location.
def knight_move(n, knight_loc):
    next_possible_locs = []
    x = knight_loc[0]
    y = knight_loc[1]

    def move(n, loc, x_move, y_move, next_loc):
        x = loc[0]
        y = loc[1]
        if (x + x_move >= 0) and (x + x_move < n):
            if (y + y_move >= 0) and (y + y_move < n):
                next_loc.append((x + x_move, y + y_move))

    # Knight can move in 8 other cells at maximum
    move(n, knight_loc, -1, -2, next_possible_locs) #1
    move(n, knight_loc, -2, +1, next_possible_locs) #3
    move(n, knight_loc, -2, -1, next_possible_locs) #2
    move(n, knight_loc, -1, +2, next_possible_locs) #4
    move(n, knight_loc, +1, +2, next_possible_locs) #5
    move(n, knight_loc, +2, +1, next_possible_locs) #6
    move(n, knight_loc, +2, -1, next_possible_locs) #7
    move(n, knight_loc, +1, -2, next_possible_locs) #8

    return next_possible_locs


def backtracking_knight(n, k, knight_loc):
    global possible_locs
    if k == 0:
        final_possible_locs.add(knight_loc)
    if k > 0:
        next_locs = knight_move(n, knight_loc)
        for loc in next_locs:
            backtracking_knight(n, k - 1, loc)




backtracking_knight(n, k, (0,0))
print(len(final_possible_locs))