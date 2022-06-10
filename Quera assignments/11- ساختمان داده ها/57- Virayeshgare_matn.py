q = int(input())
string = []
pointer = 0

for _ in range(q):
    opt = input()
    if opt == '+':
        pointer += 1
    elif opt == '-':
        pointer -= 1
    else:
        _, b = opt.split()
        string.insert(pointer, b)
        pointer += 1

print(*string, sep='')