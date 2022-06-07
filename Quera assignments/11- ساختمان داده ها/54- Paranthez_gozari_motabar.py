string = input()

# string1 = '(()(()))'
# string2 = ')(()(()))('



def solve(string):
    stack = [(string[0],1)]
    pairs = []
    for index, i in enumerate(string[1:]):
        if stack[-1][0] == '(':
            if i == ')':
                try:
                    pairs.append((stack[-1][1], index+2))
                    stack.pop()
                except:
                    pass
            else:
                stack.append((i, index+2))
        elif stack[-1][0] == ')':
            stack.append((i, index+2))
    if stack == []:
        return pairs
    else:
        return -1


# print(solve(string1))
# print(solve(string2))


ans = solve(string)
if ans == -1:
    print(-1)
else:
    for i,j in ans:
        print(f'{i} {j}')