string = input()


def solve(string):
    stack = []
    pairs = []
    for id, char in enumerate(string):
        if char == '(':
            stack.append(('(', id + 1))
        else:
            if len(stack) == 0:
                return -1
            else:
                if stack[-1][0] == '(':
                    pairs.append((stack[-1][1], id + 1))
                    stack.pop()
    if len(stack) == 0:
        return pairs
    else:
        return -1


def print_answer(ans):
    if ans == -1:
        print(-1)
    else:
        for i, j in ans:
            print(f'{i} {j}')


print_answer(solve(string))